# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v0.8.1
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from permify.models.computed_attribute import ComputedAttribute
from permify.models.computed_user_set import ComputedUserSet
from permify.models.tuple_to_user_set import TupleToUserSet
from permify.models.v1_call import V1Call
from typing import Optional, Set
from typing_extensions import Self

class Leaf(BaseModel):
    """
    Leaf represents a leaf node in the permission tree.
    """ # noqa: E501
    computed_user_set: Optional[ComputedUserSet] = Field(default=None, alias="computedUserSet")
    tuple_to_user_set: Optional[TupleToUserSet] = Field(default=None, alias="tupleToUserSet")
    computed_attribute: Optional[ComputedAttribute] = Field(default=None, alias="computedAttribute")
    call: Optional[V1Call] = None
    __properties: ClassVar[List[str]] = ["computedUserSet", "tupleToUserSet", "computedAttribute", "call"]

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
        """Create an instance of Leaf from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of computed_user_set
        if self.computed_user_set:
            _dict['computedUserSet'] = self.computed_user_set.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tuple_to_user_set
        if self.tuple_to_user_set:
            _dict['tupleToUserSet'] = self.tuple_to_user_set.to_dict()
        # override the default output from pydantic by calling `to_dict()` of computed_attribute
        if self.computed_attribute:
            _dict['computedAttribute'] = self.computed_attribute.to_dict()
        # override the default output from pydantic by calling `to_dict()` of call
        if self.call:
            _dict['call'] = self.call.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Leaf from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "computedUserSet": ComputedUserSet.from_dict(obj["computedUserSet"]) if obj.get("computedUserSet") is not None else None,
            "tupleToUserSet": TupleToUserSet.from_dict(obj["tupleToUserSet"]) if obj.get("tupleToUserSet") is not None else None,
            "computedAttribute": ComputedAttribute.from_dict(obj["computedAttribute"]) if obj.get("computedAttribute") is not None else None,
            "call": V1Call.from_dict(obj["call"]) if obj.get("call") is not None else None
        })
        return _obj


