# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v0.9.1
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class CheckResult(str, Enum):
    """
    Enumerates results of a check operation.   - CHECK_RESULT_UNSPECIFIED: Not specified check result. This is the default value.  - CHECK_RESULT_ALLOWED: Represents a successful check (the check allowed the operation).  - CHECK_RESULT_DENIED: Represents a failed check (the check denied the operation).
    """

    """
    allowed enum values
    """
    CHECK_RESULT_UNSPECIFIED = 'CHECK_RESULT_UNSPECIFIED'
    CHECK_RESULT_ALLOWED = 'CHECK_RESULT_ALLOWED'
    CHECK_RESULT_DENIED = 'CHECK_RESULT_DENIED'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CheckResult from a JSON string"""
        return cls(json.loads(json_str))


