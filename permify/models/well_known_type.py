# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v0.8.5
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class WellKnownType(str, Enum):
    """
    Well-known protobuf types treated with first-class support in CEL.   - WELL_KNOWN_TYPE_UNSPECIFIED: Unspecified type.  - ANY: Well-known protobuf.Any type.  Any types are a polymorphic message type. During type-checking they are treated like `DYN` types, but at runtime they are resolved to a specific message type specified at evaluation time.  - TIMESTAMP: Well-known protobuf.Timestamp type, internally referenced as `timestamp`.  - DURATION: Well-known protobuf.Duration type, internally referenced as `duration`.
    """

    """
    allowed enum values
    """
    WELL_KNOWN_TYPE_UNSPECIFIED = 'WELL_KNOWN_TYPE_UNSPECIFIED'
    ANY = 'ANY'
    TIMESTAMP = 'TIMESTAMP'
    DURATION = 'DURATION'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of WellKnownType from a JSON string"""
        return cls(json.loads(json_str))


