# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v1.0.1
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from permify.models.permission_lookup_entity_stream_response import PermissionLookupEntityStreamResponse

class TestPermissionLookupEntityStreamResponse(unittest.TestCase):
    """PermissionLookupEntityStreamResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PermissionLookupEntityStreamResponse:
        """Test PermissionLookupEntityStreamResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PermissionLookupEntityStreamResponse`
        """
        model = PermissionLookupEntityStreamResponse()
        if include_optional:
            return PermissionLookupEntityStreamResponse(
                entity_id = ''
            )
        else:
            return PermissionLookupEntityStreamResponse(
        )
        """

    def testPermissionLookupEntityStreamResponse(self):
        """Test PermissionLookupEntityStreamResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
