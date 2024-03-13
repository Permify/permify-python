# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v0.7.7
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.schema_api import SchemaApi


class TestSchemaApi(unittest.TestCase):
    """SchemaApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SchemaApi()

    def tearDown(self) -> None:
        pass

    def test_schemas_list(self) -> None:
        """Test case for schemas_list

        list all authorization models
        """
        pass

    def test_schemas_read(self) -> None:
        """Test case for schemas_read

        read your authorization model
        """
        pass

    def test_schemas_write(self) -> None:
        """Test case for schemas_write

        write your authorization model
        """
        pass


if __name__ == '__main__':
    unittest.main()
