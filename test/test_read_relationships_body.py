# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v1.1.1
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from permify.models.read_relationships_body import ReadRelationshipsBody

class TestReadRelationshipsBody(unittest.TestCase):
    """ReadRelationshipsBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReadRelationshipsBody:
        """Test ReadRelationshipsBody
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReadRelationshipsBody`
        """
        model = ReadRelationshipsBody()
        if include_optional:
            return ReadRelationshipsBody(
                metadata = permify.models.relationship_read_request_metadata.RelationshipReadRequestMetadata(
                    snap_token = '', ),
                filter = permify.models.tuple_filter.TupleFilter(
                    entity = permify.models.entity_filter.EntityFilter(
                        type = '', 
                        ids = [
                            ''
                            ], ), 
                    relation = '', 
                    subject = permify.models.subject_filter.SubjectFilter(
                        type = '', 
                        ids = [
                            ''
                            ], 
                        relation = '', ), ),
                page_size = 56,
                continuous_token = ''
            )
        else:
            return ReadRelationshipsBody(
        )
        """

    def testReadRelationshipsBody(self):
        """Test ReadRelationshipsBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
