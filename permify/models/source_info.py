# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v0.7.7
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from permify.models.expr import Expr
from typing import Optional, Set
from typing_extensions import Self

class SourceInfo(BaseModel):
    """
    Source information collected at parse time.
    """ # noqa: E501
    syntax_version: Optional[StrictStr] = Field(default=None, description="The syntax version of the source, e.g. `cel1`.", alias="syntaxVersion")
    location: Optional[StrictStr] = Field(default=None, description="The location name. All position information attached to an expression is relative to this location.  The location could be a file, UI element, or similar. For example, `acme/app/AnvilPolicy.cel`.")
    line_offsets: Optional[List[StrictInt]] = Field(default=None, description="Monotonically increasing list of code point offsets where newlines `\\n` appear.  The line number of a given position is the index `i` where for a given `id` the `line_offsets[i] < id_positions[id] < line_offsets[i+1]`. The column may be derivd from `id_positions[id] - line_offsets[i]`.", alias="lineOffsets")
    positions: Optional[Dict[str, StrictInt]] = Field(default=None, description="A map from the parse node id (e.g. `Expr.id`) to the code point offset within the source.")
    macro_calls: Optional[Dict[str, Expr]] = Field(default=None, description="A map from the parse node id where a macro replacement was made to the call `Expr` that resulted in a macro expansion.  For example, `has(value.field)` is a function call that is replaced by a `test_only` field selection in the AST. Likewise, the call `list.exists(e, e > 10)` translates to a comprehension expression. The key in the map corresponds to the expression id of the expanded macro, and the value is the call `Expr` that was replaced.", alias="macroCalls")
    __properties: ClassVar[List[str]] = ["syntaxVersion", "location", "lineOffsets", "positions", "macroCalls"]

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
        """Create an instance of SourceInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in macro_calls (dict)
        _field_dict = {}
        if self.macro_calls:
            for _key in self.macro_calls:
                if self.macro_calls[_key]:
                    _field_dict[_key] = self.macro_calls[_key].to_dict()
            _dict['macroCalls'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SourceInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "syntaxVersion": obj.get("syntaxVersion"),
            "location": obj.get("location"),
            "lineOffsets": obj.get("lineOffsets"),
            "positions": obj.get("positions"),
            "macroCalls": dict(
                (_k, Expr.from_dict(_v))
                for _k, _v in obj["macroCalls"].items()
            )
            if obj.get("macroCalls") is not None
            else None
        })
        return _obj

