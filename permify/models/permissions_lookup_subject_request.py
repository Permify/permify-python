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
from permify.models.context import Context
from permify.models.entity import Entity
from permify.models.permission_lookup_subject_request_metadata import PermissionLookupSubjectRequestMetadata
from permify.models.relation_reference import RelationReference
from typing import Optional, Set
from typing_extensions import Self

class PermissionsLookupSubjectRequest(BaseModel):
    """
    PermissionLookupSubjectRequest is the request message for the LookupSubject method in the Permission service.
    """ # noqa: E501
    metadata: Optional[PermissionLookupSubjectRequestMetadata] = None
    entity: Optional[Entity] = None
    permission: Optional[StrictStr] = Field(default=None, description="Permission to be checked, can be a permission or relation. Required, and must match the pattern \"^([a-zA-Z][a-zA-Z0-9_]{1,62}[a-zA-Z0-9])$\", max 64 bytes.")
    subject_reference: Optional[RelationReference] = None
    context: Optional[Context] = None
    __properties: ClassVar[List[str]] = ["metadata", "entity", "permission", "subject_reference", "context"]

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
        """Create an instance of PermissionsLookupSubjectRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of entity
        if self.entity:
            _dict['entity'] = self.entity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of subject_reference
        if self.subject_reference:
            _dict['subject_reference'] = self.subject_reference.to_dict()
        # override the default output from pydantic by calling `to_dict()` of context
        if self.context:
            _dict['context'] = self.context.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PermissionsLookupSubjectRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "metadata": PermissionLookupSubjectRequestMetadata.from_dict(obj["metadata"]) if obj.get("metadata") is not None else None,
            "entity": Entity.from_dict(obj["entity"]) if obj.get("entity") is not None else None,
            "permission": obj.get("permission"),
            "subject_reference": RelationReference.from_dict(obj["subject_reference"]) if obj.get("subject_reference") is not None else None,
            "context": Context.from_dict(obj["context"]) if obj.get("context") is not None else None
        })
        return _obj


