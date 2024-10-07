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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from permify.models.rewrite_operation import RewriteOperation
from typing import Optional, Set
from typing_extensions import Self

class Rewrite(BaseModel):
    """
    The Rewrite message represents a specific rewrite operation. This operation could be one of the following: union, intersection, or exclusion.
    """ # noqa: E501
    rewrite_operation: Optional[RewriteOperation] = Field(default=None, alias="rewriteOperation")
    children: Optional[List[Child]] = Field(default=None, description="A list of children that are operated upon by the rewrite operation.")
    __properties: ClassVar[List[str]] = ["rewriteOperation", "children"]

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
        """Create an instance of Rewrite from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in children (list)
        _items = []
        if self.children:
            for _item_children in self.children:
                if _item_children:
                    _items.append(_item_children.to_dict())
            _dict['children'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Rewrite from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "rewriteOperation": obj.get("rewriteOperation"),
            "children": [Child.from_dict(_item) for _item in obj["children"]] if obj.get("children") is not None else None
        })
        return _obj

from permify.models.child import Child
# TODO: Rewrite to not use raise_errors
Rewrite.model_rebuild(raise_errors=False)

