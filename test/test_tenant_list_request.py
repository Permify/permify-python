# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v0.8.0
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from permify.models.tenant_list_request import TenantListRequest

class TestTenantListRequest(unittest.TestCase):
    """TenantListRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TenantListRequest:
        """Test TenantListRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TenantListRequest`
        """
        model = TenantListRequest()
        if include_optional:
            return TenantListRequest(
                page_size = 56,
                continuous_token = ''
            )
        else:
            return TenantListRequest(
        )
        """

    def testTenantListRequest(self):
        """Test TenantListRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
