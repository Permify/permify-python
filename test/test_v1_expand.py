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

from permify.models.v1_expand import V1Expand

class TestV1Expand(unittest.TestCase):
    """V1Expand unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1Expand:
        """Test V1Expand
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1Expand`
        """
        model = V1Expand()
        if include_optional:
            return V1Expand(
                entity = permify.models.entity.Entity(
                    type = '', 
                    id = '', ),
                permission = '',
                arguments = [
                    permify.models.argument.Argument(
                        computed_attribute = permify.models.computed_attribute.ComputedAttribute(
                            name = '', ), 
                        context_attribute = permify.models.context_attribute.ContextAttribute(
                            name = '', ), )
                    ],
                expand = permify.models.expand_tree_node.ExpandTreeNode(
                    operation = 'OPERATION_UNION', 
                    children = [
                        permify.models.v1/expand.v1.Expand(
                            entity = permify.models.entity.Entity(
                                type = '', 
                                id = '', ), 
                            permission = '', 
                            arguments = [
                                permify.models.argument.Argument(
                                    computed_attribute = permify.models.computed_attribute.ComputedAttribute(
                                        name = '', ), 
                                    context_attribute = permify.models.context_attribute.ContextAttribute(
                                        name = '', ), )
                                ], 
                            leaf = permify.models.expand_leaf.ExpandLeaf(
                                subjects = permify.models.subjects.Subjects(), 
                                values = permify.models.values.Values(), 
                                value = {
                                    'key' : None
                                    }, ), )
                        ], ),
                leaf = permify.models.expand_leaf.ExpandLeaf(
                    subjects = permify.models.subjects.Subjects(), 
                    values = permify.models.values.Values(), 
                    value = {
                        'key' : None
                        }, )
            )
        else:
            return V1Expand(
        )
        """

    def testV1Expand(self):
        """Test V1Expand"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
