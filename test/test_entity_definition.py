# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v1.0.6
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from permify.models.entity_definition import EntityDefinition

class TestEntityDefinition(unittest.TestCase):
    """EntityDefinition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EntityDefinition:
        """Test EntityDefinition
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EntityDefinition`
        """
        model = EntityDefinition()
        if include_optional:
            return EntityDefinition(
                name = '',
                relations = {
                    'key' : permify.models.relation_definition.RelationDefinition(
                        name = '', 
                        relation_references = [
                            permify.models.relation_reference.RelationReference(
                                type = '', 
                                relation = '', )
                            ], )
                    },
                permissions = {
                    'key' : permify.models.permission_definition.PermissionDefinition(
                        name = '', 
                        child = permify.models.child.Child(
                            leaf = permify.models.leaf.Leaf(
                                computed_user_set = permify.models.computed_user_set.ComputedUserSet(
                                    relation = '', ), 
                                tuple_to_user_set = permify.models.tuple_to_user_set.TupleToUserSet(
                                    tuple_set = permify.models.tuple_set.TupleSet(
                                        relation = '', ), 
                                    computed = permify.models.computed_user_set.ComputedUserSet(
                                        relation = '', ), ), 
                                computed_attribute = permify.models.computed_attribute.ComputedAttribute(
                                    name = '', ), 
                                call = permify.models.v1/call.v1.Call(
                                    rule_name = '', 
                                    arguments = [
                                        permify.models.argument.Argument(
                                            context_attribute = permify.models.context_attribute.ContextAttribute(
                                                name = '', ), )
                                        ], ), ), 
                            rewrite = permify.models.rewrite.Rewrite(
                                rewrite_operation = 'OPERATION_UNION', 
                                children = [
                                    permify.models.child.Child()
                                    ], ), ), )
                    },
                attributes = {
                    'key' : permify.models.attribute_definition.AttributeDefinition(
                        name = '', 
                        type = 'ATTRIBUTE_TYPE_BOOLEAN', )
                    },
                references = {
                    'key' : 'REFERENCE_RELATION'
                    }
            )
        else:
            return EntityDefinition(
        )
        """

    def testEntityDefinition(self):
        """Test EntityDefinition"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
