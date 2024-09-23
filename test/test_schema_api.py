# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v1.1.1
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from permify.api.schema_api import SchemaApi


class TestSchemaApi(unittest.TestCase):
    """SchemaApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SchemaApi()

    def tearDown(self) -> None:
        pass

    def test_schemas_list(self) -> None:
        """Test case for schemas_list

        list schema
        """
        pass

    def test_schemas_partial_write(self) -> None:
        """Test case for schemas_partial_write

        partially update your authorization model
        """
        pass

    def test_schemas_read(self) -> None:
        """Test case for schemas_read

        read schema
        """
        pass

    def test_schemas_write(self) -> None:
        """Test case for schemas_write

        write schema
        """
        pass


if __name__ == '__main__':
    unittest.main()
