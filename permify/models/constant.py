# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v0.9.9
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class Constant(BaseModel):
    """
    Represents a primitive literal.  Named 'Constant' here for backwards compatibility.  This is similar as the primitives supported in the well-known type `google.protobuf.Value`, but richer so it can represent CEL's full range of primitives.  Lists and structs are not included as constants as these aggregate types may contain [Expr][google.api.expr.v1alpha1.Expr] elements which require evaluation and are thus not constant.  Examples of literals include: `\"hello\"`, `b'bytes'`, `1u`, `4.2`, `-2`, `true`, `null`.
    """ # noqa: E501
    null_value: Optional[StrictStr] = Field(default=None, description="null value.", alias="nullValue")
    bool_value: Optional[StrictBool] = Field(default=None, description="boolean value.", alias="boolValue")
    int64_value: Optional[StrictStr] = Field(default=None, description="int64 value.", alias="int64Value")
    uint64_value: Optional[StrictStr] = Field(default=None, description="uint64 value.", alias="uint64Value")
    double_value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="double value.", alias="doubleValue")
    string_value: Optional[StrictStr] = Field(default=None, description="string value.", alias="stringValue")
    bytes_value: Optional[Union[Annotated[bytes, Field(strict=True)], Annotated[str, Field(strict=True)]]] = Field(default=None, description="bytes value.", alias="bytesValue")
    duration_value: Optional[StrictStr] = Field(default=None, description="protobuf.Duration value.  Deprecated: duration is no longer considered a builtin cel type.", alias="durationValue")
    timestamp_value: Optional[datetime] = Field(default=None, description="protobuf.Timestamp value.  Deprecated: timestamp is no longer considered a builtin cel type.", alias="timestampValue")
    __properties: ClassVar[List[str]] = ["nullValue", "boolValue", "int64Value", "uint64Value", "doubleValue", "stringValue", "bytesValue", "durationValue", "timestampValue"]

    @field_validator('bytes_value')
    def bytes_value_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$", value):
            raise ValueError(r"must validate the regular expression /^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/")
        return value

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
        """Create an instance of Constant from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Constant from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "nullValue": obj.get("nullValue"),
            "boolValue": obj.get("boolValue"),
            "int64Value": obj.get("int64Value"),
            "uint64Value": obj.get("uint64Value"),
            "doubleValue": obj.get("doubleValue"),
            "stringValue": obj.get("stringValue"),
            "bytesValue": obj.get("bytesValue"),
            "durationValue": obj.get("durationValue"),
            "timestampValue": obj.get("timestampValue")
        })
        return _obj


