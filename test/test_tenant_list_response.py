# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v1.0.4
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from permify.models.tenant_list_response import TenantListResponse

class TestTenantListResponse(unittest.TestCase):
    """TenantListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TenantListResponse:
        """Test TenantListResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TenantListResponse`
        """
        model = TenantListResponse()
        if include_optional:
            return TenantListResponse(
                tenants = [
                    permify.models.tenant.Tenant(
                        id = '', 
                        name = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                continuous_token = ''
            )
        else:
            return TenantListResponse(
        )
        """

    def testTenantListResponse(self):
        """Test TenantListResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
