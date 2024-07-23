# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v0.10.1
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from permify.models.rewrite import Rewrite

class TestRewrite(unittest.TestCase):
    """Rewrite unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Rewrite:
        """Test Rewrite
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Rewrite`
        """
        model = Rewrite()
        if include_optional:
            return Rewrite(
                rewrite_operation = 'OPERATION_UNION',
                children = [
                    permify.models.child.Child(
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
                            rewrite_operation = 'OPERATION_UNION', ), )
                    ]
            )
        else:
            return Rewrite(
        )
        """

    def testRewrite(self):
        """Test Rewrite"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
