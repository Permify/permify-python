# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v0.8.1
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from permify.models.tuple import Tuple

class TestTuple(unittest.TestCase):
    """Tuple unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Tuple:
        """Test Tuple
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Tuple`
        """
        model = Tuple()
        if include_optional:
            return Tuple(
                entity = permify.models.entity.Entity(
                    type = '', 
                    id = '', ),
                relation = '',
                subject = permify.models.subject.Subject(
                    type = '', 
                    id = '', 
                    relation = '', )
            )
        else:
            return Tuple(
        )
        """

    def testTuple(self):
        """Test Tuple"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
