# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v0.8.2
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
from typing import Optional, Set
from typing_extensions import Self

class ExprCall(BaseModel):
    """
    A call expression, including calls to predefined functions and operators.  For example, `value == 10`, `size(map_value)`.
    """ # noqa: E501
    target: Optional[Expr] = None
    function: Optional[StrictStr] = Field(default=None, description="Required. The name of the function or method being called.")
    args: Optional[List[Expr]] = Field(default=None, description="The arguments.")
    __properties: ClassVar[List[str]] = ["target", "function", "args"]

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
        """Create an instance of ExprCall from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of target
        if self.target:
            _dict['target'] = self.target.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in args (list)
        _items = []
        if self.args:
            for _item in self.args:
                if _item:
                    _items.append(_item.to_dict())
            _dict['args'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ExprCall from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "target": Expr.from_dict(obj["target"]) if obj.get("target") is not None else None,
            "function": obj.get("function"),
            "args": [Expr.from_dict(_item) for _item in obj["args"]] if obj.get("args") is not None else None
        })
        return _obj

from permify.models.expr import Expr
# TODO: Rewrite to not use raise_errors
ExprCall.model_rebuild(raise_errors=False)

