# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v1.1.3
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from permify.models.permission_expand_body import PermissionExpandBody

class TestPermissionExpandBody(unittest.TestCase):
    """PermissionExpandBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PermissionExpandBody:
        """Test PermissionExpandBody
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PermissionExpandBody`
        """
        model = PermissionExpandBody()
        if include_optional:
            return PermissionExpandBody(
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
                            name = '', ), )
                    ]
            )
        else:
            return PermissionExpandBody(
        )
        """

    def testPermissionExpandBody(self):
        """Test PermissionExpandBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
