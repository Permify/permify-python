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

from permify.models.bundle_read_body import BundleReadBody

class TestBundleReadBody(unittest.TestCase):
    """BundleReadBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BundleReadBody:
        """Test BundleReadBody
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BundleReadBody`
        """
        model = BundleReadBody()
        if include_optional:
            return BundleReadBody(
                name = ''
            )
        else:
            return BundleReadBody(
        )
        """

    def testBundleReadBody(self):
        """Test BundleReadBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
