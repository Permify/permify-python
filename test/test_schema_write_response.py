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

from openapi_client.models.schema_write_response import SchemaWriteResponse

class TestSchemaWriteResponse(unittest.TestCase):
    """SchemaWriteResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SchemaWriteResponse:
        """Test SchemaWriteResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SchemaWriteResponse`
        """
        model = SchemaWriteResponse()
        if include_optional:
            return SchemaWriteResponse(
                schema_version = ''
            )
        else:
            return SchemaWriteResponse(
        )
        """

    def testSchemaWriteResponse(self):
        """Test SchemaWriteResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
