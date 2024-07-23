# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v0.10.1
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

class Select(BaseModel):
    """
    A field selection expression. e.g. `request.auth`.
    """ # noqa: E501
    operand: Optional[Expr] = None
    var_field: Optional[StrictStr] = Field(default=None, description="Required. The name of the field to select.  For example, in the select expression `request.auth`, the `auth` portion of the expression would be the `field`.", alias="field")
    test_only: Optional[StrictBool] = Field(default=None, description="Whether the select is to be interpreted as a field presence test.  This results from the macro `has(request.auth)`.", alias="testOnly")
    __properties: ClassVar[List[str]] = ["operand", "field", "testOnly"]

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
        """Create an instance of Select from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of operand
        if self.operand:
            _dict['operand'] = self.operand.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Select from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "operand": Expr.from_dict(obj["operand"]) if obj.get("operand") is not None else None,
            "field": obj.get("field"),
            "testOnly": obj.get("testOnly")
        })
        return _obj

from permify.models.expr import Expr
# TODO: Rewrite to not use raise_errors
Select.model_rebuild(raise_errors=False)

