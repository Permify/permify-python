# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v0.9.0
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from permify.models.expand_tree_node import ExpandTreeNode

class TestExpandTreeNode(unittest.TestCase):
    """ExpandTreeNode unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExpandTreeNode:
        """Test ExpandTreeNode
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExpandTreeNode`
        """
        model = ExpandTreeNode()
        if include_optional:
            return ExpandTreeNode(
                operation = 'OPERATION_UNSPECIFIED',
                children = [
                    permify.models.expand.Expand(
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
                            operation = 'OPERATION_UNSPECIFIED', 
                            children = [
                                permify.models.expand.Expand(
                                    permission = '', 
                                    leaf = permify.models.expand_leaf.ExpandLeaf(
                                        subjects = permify.models.subjects.Subjects(), 
                                        values = permify.models.values.Values(), 
                                        value = {
                                            'key' : None
                                            }, ), )
                                ], ), 
                        leaf = permify.models.expand_leaf.ExpandLeaf(), )
                    ]
            )
        else:
            return ExpandTreeNode(
        )
        """

    def testExpandTreeNode(self):
        """Test ExpandTreeNode"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
