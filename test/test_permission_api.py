# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v0.8.8
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from permify.permission_api import PermissionApi


class TestPermissionApi(unittest.TestCase):
    """PermissionApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PermissionApi()

    def tearDown(self) -> None:
        pass

    def test_permissions_check(self) -> None:
        """Test case for permissions_check

        check api
        """
        pass

    def test_permissions_expand(self) -> None:
        """Test case for permissions_expand

        expand api
        """
        pass

    def test_permissions_lookup_entity(self) -> None:
        """Test case for permissions_lookup_entity

        lookup entity
        """
        pass

    def test_permissions_lookup_entity_stream(self) -> None:
        """Test case for permissions_lookup_entity_stream

        lookup entity stream
        """
        pass

    def test_permissions_lookup_subject(self) -> None:
        """Test case for permissions_lookup_subject

        lookup-subject
        """
        pass

    def test_permissions_subject_permission(self) -> None:
        """Test case for permissions_subject_permission

        subject permission
        """
        pass


if __name__ == '__main__':
    unittest.main()
