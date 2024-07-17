# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v0.10.0
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from permify.models.tenant_delete_response import TenantDeleteResponse

class TestTenantDeleteResponse(unittest.TestCase):
    """TenantDeleteResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TenantDeleteResponse:
        """Test TenantDeleteResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TenantDeleteResponse`
        """
        model = TenantDeleteResponse()
        if include_optional:
            return TenantDeleteResponse(
                tenant = permify.models.tenant.Tenant(
                    id = '', 
                    name = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
            )
        else:
            return TenantDeleteResponse(
        )
        """

    def testTenantDeleteResponse(self):
        """Test TenantDeleteResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
