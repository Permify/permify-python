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

from permify.models.relation_definition import RelationDefinition

class TestRelationDefinition(unittest.TestCase):
    """RelationDefinition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RelationDefinition:
        """Test RelationDefinition
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RelationDefinition`
        """
        model = RelationDefinition()
        if include_optional:
            return RelationDefinition(
                name = '',
                relation_references = [
                    permify.models.relation_reference.RelationReference(
                        type = '', 
                        relation = '', )
                    ]
            )
        else:
            return RelationDefinition(
        )
        """

    def testRelationDefinition(self):
        """Test RelationDefinition"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
