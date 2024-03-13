# openapi-client
Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v0.7.7
- Package version: 1.0.0
- Generator version: 7.5.0-SNAPSHOT
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://github.com/Permify/permify/issues](https://github.com/Permify/permify/issues)

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)



# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.BundleApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    body = openapi_client.BundleDeleteRequest() # BundleDeleteRequest | 

    try:
        # delete bundle
        api_response = api_instance.bundle_delete(tenant_id, body)
        print("The response of BundleApi->bundle_delete:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BundleApi->bundle_delete: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BundleApi* | [**bundle_delete**](docs/BundleApi.md#bundle_delete) | **POST** /v1/tenants/{tenant_id}/bundle/delete | delete bundle
*BundleApi* | [**bundle_read**](docs/BundleApi.md#bundle_read) | **POST** /v1/tenants/{tenant_id}/bundle/read | read bundle
*BundleApi* | [**bundle_write**](docs/BundleApi.md#bundle_write) | **POST** /v1/tenants/{tenant_id}/bundle/write | write bundle
*DataApi* | [**bundle_run**](docs/DataApi.md#bundle_run) | **POST** /v1/tenants/{tenant_id}/data/run-bundle | run bundle
*DataApi* | [**data_attributes_read**](docs/DataApi.md#data_attributes_read) | **POST** /v1/tenants/{tenant_id}/data/attributes/read | read attribute(s)
*DataApi* | [**data_delete**](docs/DataApi.md#data_delete) | **POST** /v1/tenants/{tenant_id}/data/delete | delete data
*DataApi* | [**data_relationships_read**](docs/DataApi.md#data_relationships_read) | **POST** /v1/tenants/{tenant_id}/data/relationships/read | read relation tuple(s)
*DataApi* | [**data_write**](docs/DataApi.md#data_write) | **POST** /v1/tenants/{tenant_id}/data/write | create data
*DataApi* | [**relationships_delete**](docs/DataApi.md#relationships_delete) | **POST** /v1/tenants/{tenant_id}/relationships/delete | delete relationships
*DataApi* | [**relationships_write**](docs/DataApi.md#relationships_write) | **POST** /v1/tenants/{tenant_id}/relationships/write | create new relationships
*PermissionApi* | [**permissions_check**](docs/PermissionApi.md#permissions_check) | **POST** /v1/tenants/{tenant_id}/permissions/check | This method returns a decision about whether user can perform an permission on a certain resource.
*PermissionApi* | [**permissions_expand**](docs/PermissionApi.md#permissions_expand) | **POST** /v1/tenants/{tenant_id}/permissions/expand | expand relationships according to schema
*PermissionApi* | [**permissions_lookup_entity**](docs/PermissionApi.md#permissions_lookup_entity) | **POST** /v1/tenants/{tenant_id}/permissions/lookup-entity | Retrieve an entity by its identifier.
*PermissionApi* | [**permissions_lookup_entity_stream**](docs/PermissionApi.md#permissions_lookup_entity_stream) | **POST** /v1/tenants/{tenant_id}/permissions/lookup-entity-stream | Stream entities by their identifiers.
*PermissionApi* | [**permissions_lookup_subject**](docs/PermissionApi.md#permissions_lookup_subject) | **POST** /v1/tenants/{tenant_id}/permissions/lookup-subject | Retrieve a subject by its identifier.
*PermissionApi* | [**permissions_subject_permission**](docs/PermissionApi.md#permissions_subject_permission) | **POST** /v1/tenants/{tenant_id}/permissions/subject-permission | Retrieve permissions related to a specific subject.
*SchemaApi* | [**schemas_list**](docs/SchemaApi.md#schemas_list) | **POST** /v1/tenants/{tenant_id}/schemas/list | list all authorization models
*SchemaApi* | [**schemas_read**](docs/SchemaApi.md#schemas_read) | **POST** /v1/tenants/{tenant_id}/schemas/read | read your authorization model
*SchemaApi* | [**schemas_write**](docs/SchemaApi.md#schemas_write) | **POST** /v1/tenants/{tenant_id}/schemas/write | write your authorization model
*TenancyApi* | [**tenants_create**](docs/TenancyApi.md#tenants_create) | **POST** /v1/tenants/create | create new tenant
*TenancyApi* | [**tenants_delete**](docs/TenancyApi.md#tenants_delete) | **DELETE** /v1/tenants/{id} | delete tenant
*TenancyApi* | [**tenants_list**](docs/TenancyApi.md#tenants_list) | **POST** /v1/tenants/list | list tenants
*WatchApi* | [**watch_watch**](docs/WatchApi.md#watch_watch) | **POST** /v1/tenants/{tenant_id}/watch | 


## Documentation For Models

 - [AbstractType](docs/AbstractType.md)
 - [Any](docs/Any.md)
 - [Argument](docs/Argument.md)
 - [Attribute](docs/Attribute.md)
 - [AttributeDefinition](docs/AttributeDefinition.md)
 - [AttributeFilter](docs/AttributeFilter.md)
 - [AttributeReadRequestMetadata](docs/AttributeReadRequestMetadata.md)
 - [AttributeReadResponse](docs/AttributeReadResponse.md)
 - [AttributeType](docs/AttributeType.md)
 - [BundleDeleteRequest](docs/BundleDeleteRequest.md)
 - [BundleDeleteResponse](docs/BundleDeleteResponse.md)
 - [BundleReadRequest](docs/BundleReadRequest.md)
 - [BundleReadResponse](docs/BundleReadResponse.md)
 - [BundleRunRequest](docs/BundleRunRequest.md)
 - [BundleRunResponse](docs/BundleRunResponse.md)
 - [BundleWriteRequest](docs/BundleWriteRequest.md)
 - [BundleWriteResponse](docs/BundleWriteResponse.md)
 - [CheckResult](docs/CheckResult.md)
 - [CheckedExpr](docs/CheckedExpr.md)
 - [Child](docs/Child.md)
 - [Comprehension](docs/Comprehension.md)
 - [ComputedAttribute](docs/ComputedAttribute.md)
 - [ComputedUserSet](docs/ComputedUserSet.md)
 - [Constant](docs/Constant.md)
 - [Context](docs/Context.md)
 - [ContextAttribute](docs/ContextAttribute.md)
 - [CreateList](docs/CreateList.md)
 - [CreateStruct](docs/CreateStruct.md)
 - [DataAttributesReadRequest](docs/DataAttributesReadRequest.md)
 - [DataBundle](docs/DataBundle.md)
 - [DataChange](docs/DataChange.md)
 - [DataChangeOperation](docs/DataChangeOperation.md)
 - [DataChanges](docs/DataChanges.md)
 - [DataDeleteRequest](docs/DataDeleteRequest.md)
 - [DataDeleteResponse](docs/DataDeleteResponse.md)
 - [DataRelationshipsReadRequest](docs/DataRelationshipsReadRequest.md)
 - [DataWriteRequest](docs/DataWriteRequest.md)
 - [DataWriteRequestMetadata](docs/DataWriteRequestMetadata.md)
 - [DataWriteResponse](docs/DataWriteResponse.md)
 - [Entity](docs/Entity.md)
 - [EntityDefinition](docs/EntityDefinition.md)
 - [EntityDefinitionReference](docs/EntityDefinitionReference.md)
 - [EntityFilter](docs/EntityFilter.md)
 - [Entry](docs/Entry.md)
 - [Expand](docs/Expand.md)
 - [ExpandLeaf](docs/ExpandLeaf.md)
 - [ExpandTreeNode](docs/ExpandTreeNode.md)
 - [ExpandTreeNodeOperation](docs/ExpandTreeNodeOperation.md)
 - [Expr](docs/Expr.md)
 - [ExprCall](docs/ExprCall.md)
 - [FunctionType](docs/FunctionType.md)
 - [Ident](docs/Ident.md)
 - [Leaf](docs/Leaf.md)
 - [ListType](docs/ListType.md)
 - [MapType](docs/MapType.md)
 - [NullValue](docs/NullValue.md)
 - [PermissionCheckRequestMetadata](docs/PermissionCheckRequestMetadata.md)
 - [PermissionCheckResponse](docs/PermissionCheckResponse.md)
 - [PermissionCheckResponseMetadata](docs/PermissionCheckResponseMetadata.md)
 - [PermissionDefinition](docs/PermissionDefinition.md)
 - [PermissionExpandRequestMetadata](docs/PermissionExpandRequestMetadata.md)
 - [PermissionExpandResponse](docs/PermissionExpandResponse.md)
 - [PermissionLookupEntityRequestMetadata](docs/PermissionLookupEntityRequestMetadata.md)
 - [PermissionLookupEntityResponse](docs/PermissionLookupEntityResponse.md)
 - [PermissionLookupEntityStreamResponse](docs/PermissionLookupEntityStreamResponse.md)
 - [PermissionLookupSubjectRequestMetadata](docs/PermissionLookupSubjectRequestMetadata.md)
 - [PermissionLookupSubjectResponse](docs/PermissionLookupSubjectResponse.md)
 - [PermissionSubjectPermissionRequestMetadata](docs/PermissionSubjectPermissionRequestMetadata.md)
 - [PermissionSubjectPermissionResponse](docs/PermissionSubjectPermissionResponse.md)
 - [PermissionsCheckRequest](docs/PermissionsCheckRequest.md)
 - [PermissionsExpandRequest](docs/PermissionsExpandRequest.md)
 - [PermissionsLookupEntityRequest](docs/PermissionsLookupEntityRequest.md)
 - [PermissionsLookupSubjectRequest](docs/PermissionsLookupSubjectRequest.md)
 - [PermissionsSubjectPermissionRequest](docs/PermissionsSubjectPermissionRequest.md)
 - [PrimitiveType](docs/PrimitiveType.md)
 - [RelationDefinition](docs/RelationDefinition.md)
 - [RelationReference](docs/RelationReference.md)
 - [RelationshipDeleteRequest](docs/RelationshipDeleteRequest.md)
 - [RelationshipDeleteResponse](docs/RelationshipDeleteResponse.md)
 - [RelationshipReadRequestMetadata](docs/RelationshipReadRequestMetadata.md)
 - [RelationshipReadResponse](docs/RelationshipReadResponse.md)
 - [RelationshipWriteRequestMetadata](docs/RelationshipWriteRequestMetadata.md)
 - [RelationshipWriteResponse](docs/RelationshipWriteResponse.md)
 - [RelationshipsWriteRequest](docs/RelationshipsWriteRequest.md)
 - [Rewrite](docs/Rewrite.md)
 - [RewriteOperation](docs/RewriteOperation.md)
 - [RuleDefinition](docs/RuleDefinition.md)
 - [SchemaDefinition](docs/SchemaDefinition.md)
 - [SchemaDefinitionReference](docs/SchemaDefinitionReference.md)
 - [SchemaList](docs/SchemaList.md)
 - [SchemaListResponse](docs/SchemaListResponse.md)
 - [SchemaReadRequestMetadata](docs/SchemaReadRequestMetadata.md)
 - [SchemaReadResponse](docs/SchemaReadResponse.md)
 - [SchemaWriteResponse](docs/SchemaWriteResponse.md)
 - [SchemasListRequest](docs/SchemasListRequest.md)
 - [SchemasReadRequest](docs/SchemasReadRequest.md)
 - [SchemasWriteRequest](docs/SchemasWriteRequest.md)
 - [Select](docs/Select.md)
 - [SourceInfo](docs/SourceInfo.md)
 - [Status](docs/Status.md)
 - [StreamResultOfPermissionLookupEntityStreamResponse](docs/StreamResultOfPermissionLookupEntityStreamResponse.md)
 - [StreamResultOfWatchResponse](docs/StreamResultOfWatchResponse.md)
 - [Subject](docs/Subject.md)
 - [SubjectFilter](docs/SubjectFilter.md)
 - [Subjects](docs/Subjects.md)
 - [Tenant](docs/Tenant.md)
 - [TenantCreateRequest](docs/TenantCreateRequest.md)
 - [TenantCreateResponse](docs/TenantCreateResponse.md)
 - [TenantDeleteResponse](docs/TenantDeleteResponse.md)
 - [TenantListRequest](docs/TenantListRequest.md)
 - [TenantListResponse](docs/TenantListResponse.md)
 - [Tuple](docs/Tuple.md)
 - [TupleFilter](docs/TupleFilter.md)
 - [TupleSet](docs/TupleSet.md)
 - [TupleToUserSet](docs/TupleToUserSet.md)
 - [V1Call](docs/V1Call.md)
 - [V1Operation](docs/V1Operation.md)
 - [V1alpha1Reference](docs/V1alpha1Reference.md)
 - [V1alpha1Type](docs/V1alpha1Type.md)
 - [Values](docs/Values.md)
 - [WatchResponse](docs/WatchResponse.md)
 - [WatchWatchRequest](docs/WatchWatchRequest.md)
 - [WellKnownType](docs/WellKnownType.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="ApiKeyAuth"></a>
### ApiKeyAuth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

hello@permify.co


