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

from permify.api.tenancy_api import TenancyApi


class TestTenancyApi(unittest.TestCase):
    """TenancyApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TenancyApi()

    def tearDown(self) -> None:
        pass

    def test_tenants_create(self) -> None:
        """Test case for tenants_create

        create tenant
        """
        pass

    def test_tenants_delete(self) -> None:
        """Test case for tenants_delete

        delete tenant
        """
        pass

    def test_tenants_list(self) -> None:
        """Test case for tenants_list

        list tenants
        """
        pass


if __name__ == '__main__':
    unittest.main()
