# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v0.8.8
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

class AbstractType(BaseModel):
    """
    Application defined abstract type.
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="The fully qualified name of this abstract type.")
    parameter_types: Optional[List[V1alpha1Type]] = Field(default=None, description="Parameter types for this abstract type.", alias="parameterTypes")
    __properties: ClassVar[List[str]] = ["name", "parameterTypes"]

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
        """Create an instance of AbstractType from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in parameter_types (list)
        _items = []
        if self.parameter_types:
            for _item in self.parameter_types:
                if _item:
                    _items.append(_item.to_dict())
            _dict['parameterTypes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AbstractType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "parameterTypes": [V1alpha1Type.from_dict(_item) for _item in obj["parameterTypes"]] if obj.get("parameterTypes") is not None else None
        })
        return _obj

from permify.models.v1alpha1_type import V1alpha1Type
# TODO: Rewrite to not use raise_errors
AbstractType.model_rebuild(raise_errors=False)

