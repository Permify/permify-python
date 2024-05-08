# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v0.8.4
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from permify.models.data_relationships_read_request import DataRelationshipsReadRequest

class TestDataRelationshipsReadRequest(unittest.TestCase):
    """DataRelationshipsReadRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataRelationshipsReadRequest:
        """Test DataRelationshipsReadRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataRelationshipsReadRequest`
        """
        model = DataRelationshipsReadRequest()
        if include_optional:
            return DataRelationshipsReadRequest(
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
            return DataRelationshipsReadRequest(
        )
        """

    def testDataRelationshipsReadRequest(self):
        """Test DataRelationshipsReadRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
