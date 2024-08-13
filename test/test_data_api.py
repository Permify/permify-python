# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v1.0.0
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from permify.api.data_api import DataApi


class TestDataApi(unittest.TestCase):
    """DataApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DataApi()

    def tearDown(self) -> None:
        pass

    def test_bundle_run(self) -> None:
        """Test case for bundle_run

        run bundle
        """
        pass

    def test_data_attributes_read(self) -> None:
        """Test case for data_attributes_read

        read attributes
        """
        pass

    def test_data_delete(self) -> None:
        """Test case for data_delete

        delete data
        """
        pass

    def test_data_relationships_read(self) -> None:
        """Test case for data_relationships_read

        read relationships
        """
        pass

    def test_data_write(self) -> None:
        """Test case for data_write

        write data
        """
        pass

    def test_relationships_delete(self) -> None:
        """Test case for relationships_delete

        delete relationships
        """
        pass

    def test_relationships_write(self) -> None:
        """Test case for relationships_write

        write relationships
        """
        pass


if __name__ == '__main__':
    unittest.main()
