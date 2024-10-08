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

from permify.api.bundle_api import BundleApi


class TestBundleApi(unittest.TestCase):
    """BundleApi unit test stubs"""

    def setUp(self) -> None:
        self.api = BundleApi()

    def tearDown(self) -> None:
        pass

    def test_bundle_delete(self) -> None:
        """Test case for bundle_delete

        delete bundle
        """
        pass

    def test_bundle_read(self) -> None:
        """Test case for bundle_read

        read bundle
        """
        pass

    def test_bundle_write(self) -> None:
        """Test case for bundle_write

        write bundle
        """
        pass


if __name__ == '__main__':
    unittest.main()
