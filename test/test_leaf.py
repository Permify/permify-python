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

from permify.models.leaf import Leaf

class TestLeaf(unittest.TestCase):
    """Leaf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Leaf:
        """Test Leaf
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Leaf`
        """
        model = Leaf()
        if include_optional:
            return Leaf(
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
                            computed_attribute = permify.models.computed_attribute.ComputedAttribute(
                                name = '', ), )
                        ], )
            )
        else:
            return Leaf(
        )
        """

    def testLeaf(self):
        """Test Leaf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
