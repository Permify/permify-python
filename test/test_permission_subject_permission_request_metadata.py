# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v0.8.7
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from permify.models.permission_subject_permission_request_metadata import PermissionSubjectPermissionRequestMetadata

class TestPermissionSubjectPermissionRequestMetadata(unittest.TestCase):
    """PermissionSubjectPermissionRequestMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PermissionSubjectPermissionRequestMetadata:
        """Test PermissionSubjectPermissionRequestMetadata
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PermissionSubjectPermissionRequestMetadata`
        """
        model = PermissionSubjectPermissionRequestMetadata()
        if include_optional:
            return PermissionSubjectPermissionRequestMetadata(
                schema_version = '',
                snap_token = '',
                only_permission = True,
                depth = 56
            )
        else:
            return PermissionSubjectPermissionRequestMetadata(
        )
        """

    def testPermissionSubjectPermissionRequestMetadata(self):
        """Test PermissionSubjectPermissionRequestMetadata"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
