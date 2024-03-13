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

from openapi_client.models.permissions_expand_request import PermissionsExpandRequest

class TestPermissionsExpandRequest(unittest.TestCase):
    """PermissionsExpandRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PermissionsExpandRequest:
        """Test PermissionsExpandRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PermissionsExpandRequest`
        """
        model = PermissionsExpandRequest()
        if include_optional:
            return PermissionsExpandRequest(
                metadata = openapi_client.models.permission_expand_request_metadata.PermissionExpandRequestMetadata(
                    schema_version = '', 
                    snap_token = '', ),
                entity = openapi_client.models.entity.Entity(
                    type = '', 
                    id = '', ),
                permission = '',
                context = openapi_client.models.context.Context(
                    tuples = [
                        openapi_client.models.tuple.Tuple(
                            entity = openapi_client.models.entity.Entity(
                                type = '', 
                                id = '', ), 
                            relation = '', 
                            subject = openapi_client.models.subject.Subject(
                                type = '', 
                                id = '', 
                                relation = '', ), )
                        ], 
                    attributes = [
                        openapi_client.models.attribute.Attribute(
                            attribute = '', 
                            value = {
                                'key' : None
                                }, )
                        ], 
                    data = openapi_client.models.data.data(), ),
                arguments = [
                    openapi_client.models.argument.Argument(
                        computed_attribute = openapi_client.models.computed_attribute.ComputedAttribute(
                            name = '', ), 
                        context_attribute = openapi_client.models.context_attribute.ContextAttribute(
                            name = '', ), )
                    ]
            )
        else:
            return PermissionsExpandRequest(
        )
        """

    def testPermissionsExpandRequest(self):
        """Test PermissionsExpandRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
