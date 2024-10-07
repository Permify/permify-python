# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v1.1.3
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from permify.models.permission_expand_response import PermissionExpandResponse

class TestPermissionExpandResponse(unittest.TestCase):
    """PermissionExpandResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PermissionExpandResponse:
        """Test PermissionExpandResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PermissionExpandResponse`
        """
        model = PermissionExpandResponse()
        if include_optional:
            return PermissionExpandResponse(
                tree = permify.models.v1/expand.v1.Expand(
                    entity = permify.models.entity.Entity(
                        type = '', 
                        id = '', ), 
                    permission = '', 
                    arguments = [
                        permify.models.argument.Argument(
                            computed_attribute = permify.models.computed_attribute.ComputedAttribute(
                                name = '', ), )
                        ], 
                    expand = permify.models.expand_tree_node.ExpandTreeNode(
                        operation = 'OPERATION_UNION', 
                        children = [
                            permify.models.v1/expand.v1.Expand(
                                permission = '', 
                                leaf = permify.models.expand_leaf.ExpandLeaf(
                                    subjects = permify.models.subjects.Subjects(), 
                                    values = permify.models.values.Values(), 
                                    value = {
                                        'key' : None
                                        }, ), )
                            ], ), 
                    leaf = permify.models.expand_leaf.ExpandLeaf(), )
            )
        else:
            return PermissionExpandResponse(
        )
        """

    def testPermissionExpandResponse(self):
        """Test PermissionExpandResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
