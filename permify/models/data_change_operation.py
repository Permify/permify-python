# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v1.0.5
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class DataChangeOperation(str, Enum):
    """
     - OPERATION_CREATE: Creation operation.  - OPERATION_DELETE: Deletion operation.
    """

    """
    allowed enum values
    """
    OPERATION_CREATE = 'OPERATION_CREATE'
    OPERATION_DELETE = 'OPERATION_DELETE'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DataChangeOperation from a JSON string"""
        return cls(json.loads(json_str))


