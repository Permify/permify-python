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

from permify.models.argument import Argument

class TestArgument(unittest.TestCase):
    """Argument unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Argument:
        """Test Argument
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Argument`
        """
        model = Argument()
        if include_optional:
            return Argument(
                computed_attribute = permify.models.computed_attribute.ComputedAttribute(
                    name = '', )
            )
        else:
            return Argument(
        )
        """

    def testArgument(self):
        """Test Argument"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
