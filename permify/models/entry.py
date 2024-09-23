# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v1.1.1
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Entry(BaseModel):
    """
    Represents an entry.
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Required. An id assigned to this node by the parser which is unique in a given expression tree. This is used to associate type information and other attributes to the node.")
    field_key: Optional[StrictStr] = Field(default=None, description="The field key for a message creator statement.", alias="fieldKey")
    map_key: Optional[Expr] = Field(default=None, alias="mapKey")
    value: Optional[Expr] = None
    optional_entry: Optional[StrictBool] = Field(default=None, description="Whether the key-value pair is optional.", alias="optionalEntry")
    __properties: ClassVar[List[str]] = ["id", "fieldKey", "mapKey", "value", "optionalEntry"]

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
        """Create an instance of Entry from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of map_key
        if self.map_key:
            _dict['mapKey'] = self.map_key.to_dict()
        # override the default output from pydantic by calling `to_dict()` of value
        if self.value:
            _dict['value'] = self.value.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Entry from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "fieldKey": obj.get("fieldKey"),
            "mapKey": Expr.from_dict(obj["mapKey"]) if obj.get("mapKey") is not None else None,
            "value": Expr.from_dict(obj["value"]) if obj.get("value") is not None else None,
            "optionalEntry": obj.get("optionalEntry")
        })
        return _obj

from permify.models.expr import Expr
# TODO: Rewrite to not use raise_errors
Entry.model_rebuild(raise_errors=False)

