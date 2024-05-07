# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v0.8.3
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
from permify.models.attribute_filter import AttributeFilter
from permify.models.attribute_read_request_metadata import AttributeReadRequestMetadata
from typing import Optional, Set
from typing_extensions import Self

class DataAttributesReadRequest(BaseModel):
    """
    AttributeReadRequest defines the structure of a request for reading attributes. It includes the tenant_id, metadata, attribute filter, page size for pagination, and a continuous token for multi-page results.
    """ # noqa: E501
    metadata: Optional[AttributeReadRequestMetadata] = None
    filter: Optional[AttributeFilter] = None
    page_size: Optional[StrictInt] = Field(default=None, description="page_size specifies the number of results to return in a single page. If more results are available, a continuous_token is included in the response.")
    continuous_token: Optional[StrictStr] = Field(default=None, description="continuous_token is used in case of paginated reads to get the next page of results.")
    __properties: ClassVar[List[str]] = ["metadata", "filter", "page_size", "continuous_token"]

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
        """Create an instance of DataAttributesReadRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of filter
        if self.filter:
            _dict['filter'] = self.filter.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataAttributesReadRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "metadata": AttributeReadRequestMetadata.from_dict(obj["metadata"]) if obj.get("metadata") is not None else None,
            "filter": AttributeFilter.from_dict(obj["filter"]) if obj.get("filter") is not None else None,
            "page_size": obj.get("page_size"),
            "continuous_token": obj.get("continuous_token")
        })
        return _obj


