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

from permify.models.permissions_expand_request import PermissionsExpandRequest

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
                metadata = permify.models.permission_expand_request_metadata.PermissionExpandRequestMetadata(
                    schema_version = '', 
                    snap_token = '', ),
                entity = permify.models.entity.Entity(
                    type = '', 
                    id = '', ),
                permission = '',
                context = permify.models.context.Context(
                    tuples = [
                        permify.models.tuple.Tuple(
                            entity = permify.models.entity.Entity(
                                type = '', 
                                id = '', ), 
                            relation = '', 
                            subject = permify.models.subject.Subject(
                                type = '', 
                                id = '', 
                                relation = '', ), )
                        ], 
                    attributes = [
                        permify.models.attribute.Attribute(
                            attribute = '', 
                            value = {
                                'key' : None
                                }, )
                        ], 
                    data = permify.models.data.data(), ),
                arguments = [
                    permify.models.argument.Argument(
                        computed_attribute = permify.models.computed_attribute.ComputedAttribute(
                            name = '', ), 
                        context_attribute = permify.models.context_attribute.ContextAttribute(
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