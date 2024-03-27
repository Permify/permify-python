# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v0.7.9
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from permify.models.entity_filter import EntityFilter

class TestEntityFilter(unittest.TestCase):
    """EntityFilter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EntityFilter:
        """Test EntityFilter
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EntityFilter`
        """
        model = EntityFilter()
        if include_optional:
            return EntityFilter(
                type = '',
                ids = [
                    ''
                    ]
            )
        else:
            return EntityFilter(
        )
        """

    def testEntityFilter(self):
        """Test EntityFilter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
