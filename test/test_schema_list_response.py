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

from openapi_client.models.schema_list_response import SchemaListResponse

class TestSchemaListResponse(unittest.TestCase):
    """SchemaListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SchemaListResponse:
        """Test SchemaListResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SchemaListResponse`
        """
        model = SchemaListResponse()
        if include_optional:
            return SchemaListResponse(
                head = '',
                schemas = [
                    openapi_client.models.schema_list_provides_a_list_of_schema_versions_with_their_corresponding_creation_timestamps.SchemaList provides a list of schema versions with their corresponding creation timestamps(
                        version = '', 
                        created_at = '', )
                    ],
                continuous_token = ''
            )
        else:
            return SchemaListResponse(
        )
        """

    def testSchemaListResponse(self):
        """Test SchemaListResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
