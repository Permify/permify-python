# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v1.0.3
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class SchemaDefinitionReference(str, Enum):
    """
    The Reference enum helps distinguish whether a name corresponds to an entity or a rule.   - REFERENCE_ENTITY: Indicates that the name refers to an entity.  - REFERENCE_RULE: Indicates that the name refers to a rule.
    """

    """
    allowed enum values
    """
    REFERENCE_ENTITY = 'REFERENCE_ENTITY'
    REFERENCE_RULE = 'REFERENCE_RULE'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SchemaDefinitionReference from a JSON string"""
        return cls(json.loads(json_str))


