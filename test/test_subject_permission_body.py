# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v1.0.4
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from permify.models.subject_permission_body import SubjectPermissionBody

class TestSubjectPermissionBody(unittest.TestCase):
    """SubjectPermissionBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SubjectPermissionBody:
        """Test SubjectPermissionBody
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SubjectPermissionBody`
        """
        model = SubjectPermissionBody()
        if include_optional:
            return SubjectPermissionBody(
                metadata = permify.models.permission_subject_permission_request_metadata.PermissionSubjectPermissionRequestMetadata(
                    schema_version = '', 
                    snap_token = '', 
                    only_permission = True, 
                    depth = 56, ),
                entity = permify.models.entity.Entity(
                    type = '', 
                    id = '', ),
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
            return SubjectPermissionBody(
        )
        """

    def testSubjectPermissionBody(self):
        """Test SubjectPermissionBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
