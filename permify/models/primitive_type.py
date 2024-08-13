# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v1.0.0
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class PrimitiveType(str, Enum):
    """
    CEL primitive types.   - BOOL: Boolean type.  - INT64: Int64 type.  Proto-based integer values are widened to int64.  - UINT64: Uint64 type.  Proto-based unsigned integer values are widened to uint64.  - DOUBLE: Double type.  Proto-based float values are widened to double values.  - STRING: String type.  - BYTES: Bytes type.
    """

    """
    allowed enum values
    """
    BOOL = 'BOOL'
    INT64 = 'INT64'
    UINT64 = 'UINT64'
    DOUBLE = 'DOUBLE'
    STRING = 'STRING'
    BYTES = 'BYTES'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of PrimitiveType from a JSON string"""
        return cls(json.loads(json_str))


