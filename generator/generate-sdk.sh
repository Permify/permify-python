#!/bin/bash

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="${SCRIPT_DIR}/.."
DEFAULT_OPENAPI_FILE="${SCRIPT_DIR}/openapi.json"
DEFAULT_PACKAGE_NAME="permify"
DEFAULT_CLIENT_NAME="PermifyClient"

usage() {
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Generate Python SDK from OpenAPI specification and update project directories"
    echo ""
    echo "Options:"
    echo "  -i, --input FILE        OpenAPI JSON file (default: ${DEFAULT_OPENAPI_FILE})"
    echo "  -p, --package NAME      Python package name (default: ${DEFAULT_PACKAGE_NAME})"
    echo "  -c, --client NAME       Client class name (default: ${DEFAULT_CLIENT_NAME})"
    echo "  -h, --help              Show this help message"
    echo ""
    echo "This script will update the following:"
    echo "  - ../permify (generated Python package)"
    echo "  - ../docs (API documentation)"
    echo "  - ../test (generated tests)"
    echo "  - ../setup.py (package metadata and dependencies)"
    echo "  - ../pyproject.toml (package metadata and dependencies)"
    echo ""
    echo "Examples:"
    echo "  $0                                    # Use defaults"
    echo "  $0 -i swagger.json                   # Custom input file"
    echo "  $0 -p custom_package                 # Custom package name"
}

OPENAPI_FILE="${DEFAULT_OPENAPI_FILE}"
PACKAGE_NAME="${DEFAULT_PACKAGE_NAME}"
CLIENT_NAME="${DEFAULT_CLIENT_NAME}"

while [[ $# -gt 0 ]]; do
    case $1 in
        -i|--input)
            OPENAPI_FILE="$2"
            shift 2
            ;;
        -p|--package)
            PACKAGE_NAME="$2"
            shift 2
            ;;
        -c|--client)
            CLIENT_NAME="$2"
            shift 2
            ;;
        -h|--help)
            usage
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            usage
            exit 1
            ;;
    esac
done

if [[ ! -f "${OPENAPI_FILE}" ]]; then
    echo "Error: OpenAPI file '${OPENAPI_FILE}' not found"
    exit 1
fi

# Check if Java is available
if ! command -v java &> /dev/null; then
    echo "Error: Java is required but not installed"
    exit 1
fi

TEMP_OUTPUT_DIR=$(mktemp -d)
trap 'rm -rf "${TEMP_OUTPUT_DIR}"' EXIT

OPENAPI_ABSOLUTE_PATH=$(realpath "${OPENAPI_FILE}")

OPENAPI_VERSION=$(grep -o '"version": *"[^"]*"' "${OPENAPI_FILE}" | cut -d '"' -f 4)
if [[ -z "${OPENAPI_VERSION}" ]]; then
    echo "Error: Could not extract version from OpenAPI file"
    exit 1
fi

echo "Generating Python SDK..."
echo "  OpenAPI file: ${OPENAPI_ABSOLUTE_PATH}"
echo "  OpenAPI version: ${OPENAPI_VERSION}"
echo "  Package name: ${PACKAGE_NAME}"
echo "  Client name: ${CLIENT_NAME}"
echo "  Temp directory: ${TEMP_OUTPUT_DIR}"
echo ""

# Download OpenAPI Generator CLI JAR if not present
GENERATOR_JAR="${SCRIPT_DIR}/openapi-generator-cli.jar"
if [[ ! -f "${GENERATOR_JAR}" ]]; then
    echo "Downloading OpenAPI Generator CLI..."
    curl -L -o "${GENERATOR_JAR}" https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/7.2.0/openapi-generator-cli-7.2.0.jar
fi

# Generate SDK using OpenAPI Generator CLI
java -jar "${GENERATOR_JAR}" generate \
    -i "${OPENAPI_ABSOLUTE_PATH}" \
    -g python \
    -o "${TEMP_OUTPUT_DIR}" \
    --package-name="${PACKAGE_NAME}" \
    --additional-properties=packageName="${PACKAGE_NAME}" \
    --additional-properties=clientPackage="${PACKAGE_NAME}" \
    --additional-properties=projectName="${PACKAGE_NAME}" \
    --additional-properties=packageUrl="https://github.com/Permify/permify-python" \
    --additional-properties=packageVersion="${OPENAPI_VERSION}" \
    --additional-properties=packageDescription="""Permify is an open source authorization service for creating fine-grained and scalable authorization systems.""" \
    --additional-properties=library=urllib3 \
    --additional-properties=hideGenerationTimestamp=true \
    --additional-properties=generateSourceCodeOnly=false \
    --additional-properties=licenseName="Apache-2.0" \
    --skip-validate-spec

if [[ $? -ne 0 ]]; then
    echo ""
    echo "❌ Failed to generate Python SDK"
    exit 1
fi

echo "Updating project directories..."

# Update the main package directory
PACKAGE_DIR="${PROJECT_ROOT}/${PACKAGE_NAME}"
if [[ -d "${TEMP_OUTPUT_DIR}/${PACKAGE_NAME}" ]]; then
    echo "  Updating ${PACKAGE_DIR}"
    # Backup any custom files that shouldn't be overwritten
    if [[ -f "${PACKAGE_DIR}/py.typed" ]]; then
        cp "${PACKAGE_DIR}/py.typed" "${TEMP_OUTPUT_DIR}/${PACKAGE_NAME}/py.typed"
    fi
    
    rm -rf "${PACKAGE_DIR}"
    cp -r "${TEMP_OUTPUT_DIR}/${PACKAGE_NAME}" "${PACKAGE_DIR}"
fi

# Update documentation
DOCS_DIR="${PROJECT_ROOT}/docs"
if [[ -d "${TEMP_OUTPUT_DIR}/docs" ]]; then
    echo "  Updating ${DOCS_DIR}"
    rm -rf "${DOCS_DIR}"/*.md
    mkdir -p "${DOCS_DIR}"
    cp "${TEMP_OUTPUT_DIR}/docs/"*.md "${DOCS_DIR}/"
fi

# Update tests
TEST_DIR="${PROJECT_ROOT}/test"
if [[ -d "${TEMP_OUTPUT_DIR}/test" ]]; then
    echo "  Updating ${TEST_DIR}"
    rm -rf "${TEST_DIR}"
    mkdir -p "${TEST_DIR}"
    cp -r "${TEMP_OUTPUT_DIR}/test/"* "${TEST_DIR}/"
fi

# Function to update setup.py with repository information
update_setup_py() {
    local generated_setup="${TEMP_OUTPUT_DIR}/setup.py"
    local target_setup="${PROJECT_ROOT}/setup.py"
    
    if [[ ! -f "${generated_setup}" ]]; then
        echo "    ⚠️  Warning: Generated setup.py not found, skipping update"
        return
    fi
    
    echo "  Updating setup.py"
    
    # Create a backup
    if [[ -f "${target_setup}" ]]; then
        cp "${target_setup}" "${target_setup}.bak"
    fi
    
    # Directly copy the generated setup.py without any modifications
    cp "${generated_setup}" "${target_setup}"
    
    echo "    ✅ Updated setup.py"
}

# Function to update pyproject.toml
update_pyproject_toml() {
    local target_pyproject="${PROJECT_ROOT}/pyproject.toml"
    
    if [[ ! -f "${target_pyproject}" ]]; then
        echo "    ⚠️  Warning: pyproject.toml not found, skipping update"
        return
    fi
    
    echo "  Updating pyproject.toml version"
    
    # Strip 'v' prefix from version if present
    VERSION_WITHOUT_V="${OPENAPI_VERSION#v}"
    
    # Update version in pyproject.toml
    if [[ "$OSTYPE" == "darwin"* ]]; then
        sed -i '' "s/^version = \"[^\"]*\"/version = \"${VERSION_WITHOUT_V}\"/" "${target_pyproject}"
    else
        sed -i "s/^version = \"[^\"]*\"/version = \"${VERSION_WITHOUT_V}\"/" "${target_pyproject}"
    fi
    
    echo "    ✅ Updated pyproject.toml version to ${VERSION_WITHOUT_V}"
}

# Function to extract and update requirements
update_requirements() {
    local generated_requirements="${TEMP_OUTPUT_DIR}/requirements.txt"
    local target_requirements="${PROJECT_ROOT}/requirements.txt"
    
    if [[ -f "${generated_requirements}" ]] && [[ -f "${target_requirements}" ]]; then
        echo "  Updating requirements.txt"
        
        # Create backup
        cp "${target_requirements}" "${target_requirements}.bak"
        
        # Extract non-dev requirements from generated file
        grep -v "pytest\|tox\|flake8" "${generated_requirements}" > "${target_requirements}" || true
        
        echo "    ✅ Updated requirements.txt"
    fi
}

# Update package files
update_setup_py
update_pyproject_toml
update_requirements

echo ""
echo "✅ Python SDK updated successfully!"
echo "📁 Updated directories:"
echo "   - ${PACKAGE_DIR}"
echo "   - ${DOCS_DIR}"
echo "   - ${TEST_DIR}"
echo "📝 Updated version to ${VERSION_WITHOUT_V}"
echo "🔗 Updated package configuration in:"
echo "   - setup.py"
echo "   - pyproject.toml"
echo "   - requirements.txt"