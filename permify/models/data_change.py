# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v0.9.0
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from permify.models.attribute import Attribute
from permify.models.data_change_operation import DataChangeOperation
from permify.models.tuple import Tuple
from typing import Optional, Set
from typing_extensions import Self

class DataChange(BaseModel):
    """
    DataChange represents a single change in data, with an operation type and the actual change which could be a tuple or an attribute.
    """ # noqa: E501
    operation: Optional[DataChangeOperation] = None
    tuple: Optional[Tuple] = None
    attribute: Optional[Attribute] = None
    __properties: ClassVar[List[str]] = ["operation", "tuple", "attribute"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of DataChange from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of tuple
        if self.tuple:
            _dict['tuple'] = self.tuple.to_dict()
        # override the default output from pydantic by calling `to_dict()` of attribute
        if self.attribute:
            _dict['attribute'] = self.attribute.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataChange from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "operation": obj.get("operation"),
            "tuple": Tuple.from_dict(obj["tuple"]) if obj.get("tuple") is not None else None,
            "attribute": Attribute.from_dict(obj["attribute"]) if obj.get("attribute") is not None else None
        })
        return _obj


