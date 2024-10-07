# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v1.1.3
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from permify.models.v1_operation import V1Operation
from typing import Optional, Set
from typing_extensions import Self

class DataBundle(BaseModel):
    """
    DataBundle is a message representing a bundle of data, which includes a name, a list of arguments, and a series of operations.
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="'name' is a simple string field representing the name of the DataBundle.")
    arguments: Optional[List[StrictStr]] = Field(default=None, description="'arguments' is a repeated field, which means it can contain multiple strings. These are used to store a list of arguments related to the DataBundle.")
    operations: Optional[List[V1Operation]] = Field(default=None, description="'operations' is a repeated field containing multiple Operation messages. Each Operation represents a specific action or set of actions to be performed.")
    __properties: ClassVar[List[str]] = ["name", "arguments", "operations"]

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
        """Create an instance of DataBundle from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in operations (list)
        _items = []
        if self.operations:
            for _item_operations in self.operations:
                if _item_operations:
                    _items.append(_item_operations.to_dict())
            _dict['operations'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataBundle from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "arguments": obj.get("arguments"),
            "operations": [V1Operation.from_dict(_item) for _item in obj["operations"]] if obj.get("operations") is not None else None
        })
        return _obj


