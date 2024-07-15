# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v0.9.9
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class RewriteOperation(str, Enum):
    """
    Operation enum includes potential rewrite operations. OPERATION_UNION: Represents a union operation. OPERATION_INTERSECTION: Represents an intersection operation. OPERATION_EXCLUSION: Represents an exclusion operation.   - OPERATION_UNION: Represents a union operation.  - OPERATION_INTERSECTION: Represents an intersection operation.  - OPERATION_EXCLUSION: Represents an exclusion operation.
    """

    """
    allowed enum values
    """
    OPERATION_UNION = 'OPERATION_UNION'
    OPERATION_INTERSECTION = 'OPERATION_INTERSECTION'
    OPERATION_EXCLUSION = 'OPERATION_EXCLUSION'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of RewriteOperation from a JSON string"""
        return cls(json.loads(json_str))


