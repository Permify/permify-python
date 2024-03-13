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

from openapi_client.models.permissions_subject_permission_request import PermissionsSubjectPermissionRequest

class TestPermissionsSubjectPermissionRequest(unittest.TestCase):
    """PermissionsSubjectPermissionRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PermissionsSubjectPermissionRequest:
        """Test PermissionsSubjectPermissionRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PermissionsSubjectPermissionRequest`
        """
        model = PermissionsSubjectPermissionRequest()
        if include_optional:
            return PermissionsSubjectPermissionRequest(
                metadata = openapi_client.models.permission_subject_permission_request_metadata.PermissionSubjectPermissionRequestMetadata(
                    schema_version = '', 
                    snap_token = '', 
                    only_permission = True, 
                    depth = 56, ),
                entity = openapi_client.models.entity.Entity(
                    type = '', 
                    id = '', ),
                subject = openapi_client.models.subject.Subject(
                    type = '', 
                    id = '', 
                    relation = '', ),
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
                    data = openapi_client.models.data.data(), )
            )
        else:
            return PermissionsSubjectPermissionRequest(
        )
        """

    def testPermissionsSubjectPermissionRequest(self):
        """Test PermissionsSubjectPermissionRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
