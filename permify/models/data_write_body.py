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
from permify.models.attribute import Attribute
from permify.models.data_write_request_metadata import DataWriteRequestMetadata
from permify.models.tuple import Tuple
from typing import Optional, Set
from typing_extensions import Self

class DataWriteBody(BaseModel):
    """
    DataWriteRequest defines the structure of a request for writing data. It contains the necessary information such as tenant_id, metadata, tuples and attributes for the write operation.
    """ # noqa: E501
    metadata: Optional[DataWriteRequestMetadata] = None
    tuples: Optional[List[Tuple]] = Field(default=None, description="tuples contains the list of tuples (entity-relation-entity triples) that need to be written.")
    attributes: Optional[List[Attribute]] = Field(default=None, description="attributes contains the list of attributes (entity-attribute-value triples) that need to be written.")
    __properties: ClassVar[List[str]] = ["metadata", "tuples", "attributes"]

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
        """Create an instance of DataWriteBody from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in tuples (list)
        _items = []
        if self.tuples:
            for _item_tuples in self.tuples:
                if _item_tuples:
                    _items.append(_item_tuples.to_dict())
            _dict['tuples'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in attributes (list)
        _items = []
        if self.attributes:
            for _item_attributes in self.attributes:
                if _item_attributes:
                    _items.append(_item_attributes.to_dict())
            _dict['attributes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataWriteBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "metadata": DataWriteRequestMetadata.from_dict(obj["metadata"]) if obj.get("metadata") is not None else None,
            "tuples": [Tuple.from_dict(_item) for _item in obj["tuples"]] if obj.get("tuples") is not None else None,
            "attributes": [Attribute.from_dict(_item) for _item in obj["attributes"]] if obj.get("attributes") is not None else None
        })
        return _obj


