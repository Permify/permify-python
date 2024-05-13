# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v0.8.5
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from permify.models.relationships_write_request import RelationshipsWriteRequest

class TestRelationshipsWriteRequest(unittest.TestCase):
    """RelationshipsWriteRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RelationshipsWriteRequest:
        """Test RelationshipsWriteRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RelationshipsWriteRequest`
        """
        model = RelationshipsWriteRequest()
        if include_optional:
            return RelationshipsWriteRequest(
                metadata = permify.models.relationship_write_request_metadata.RelationshipWriteRequestMetadata(
                    schema_version = '', ),
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
                    ]
            )
        else:
            return RelationshipsWriteRequest(
        )
        """

    def testRelationshipsWriteRequest(self):
        """Test RelationshipsWriteRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
