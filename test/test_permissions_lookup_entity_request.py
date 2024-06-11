# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v0.9.1
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from permify.models.permissions_lookup_entity_request import PermissionsLookupEntityRequest

class TestPermissionsLookupEntityRequest(unittest.TestCase):
    """PermissionsLookupEntityRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PermissionsLookupEntityRequest:
        """Test PermissionsLookupEntityRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PermissionsLookupEntityRequest`
        """
        model = PermissionsLookupEntityRequest()
        if include_optional:
            return PermissionsLookupEntityRequest(
                metadata = permify.models.permission_lookup_entity_request_metadata.PermissionLookupEntityRequestMetadata(
                    schema_version = '', 
                    snap_token = '', 
                    depth = 56, ),
                entity_type = '',
                permission = '',
                subject = permify.models.subject.Subject(
                    type = '', 
                    id = '', 
                    relation = '', ),
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
                    data = permify.models.data.data(), )
            )
        else:
            return PermissionsLookupEntityRequest(
        )
        """

    def testPermissionsLookupEntityRequest(self):
        """Test PermissionsLookupEntityRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
