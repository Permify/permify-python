# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v0.9.1
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
from permify.models.attribute_definition import AttributeDefinition
from permify.models.entity_definition_reference import EntityDefinitionReference
from permify.models.permission_definition import PermissionDefinition
from permify.models.relation_definition import RelationDefinition
from typing import Optional, Set
from typing_extensions import Self

class EntityDefinition(BaseModel):
    """
    The EntityDefinition message provides detailed information about a specific entity.
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="The name of the entity, which follows a specific string pattern and has a maximum byte size.")
    relations: Optional[Dict[str, RelationDefinition]] = Field(default=None, description="Map of relation definitions within this entity. The key is the relation name, and the value is the RelationDefinition.")
    permissions: Optional[Dict[str, PermissionDefinition]] = Field(default=None, description="Map of permission definitions within this entity. The key is the permission name, and the value is the PermissionDefinition.")
    attributes: Optional[Dict[str, AttributeDefinition]] = Field(default=None, description="Map of attribute definitions within this entity. The key is the attribute name, and the value is the AttributeDefinition.")
    references: Optional[Dict[str, EntityDefinitionReference]] = Field(default=None, description="Map of references indicating whether a string pertains to a relation, permission, or attribute.")
    __properties: ClassVar[List[str]] = ["name", "relations", "permissions", "attributes", "references"]

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
        """Create an instance of EntityDefinition from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in relations (dict)
        _field_dict = {}
        if self.relations:
            for _key in self.relations:
                if self.relations[_key]:
                    _field_dict[_key] = self.relations[_key].to_dict()
            _dict['relations'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in permissions (dict)
        _field_dict = {}
        if self.permissions:
            for _key in self.permissions:
                if self.permissions[_key]:
                    _field_dict[_key] = self.permissions[_key].to_dict()
            _dict['permissions'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in attributes (dict)
        _field_dict = {}
        if self.attributes:
            for _key in self.attributes:
                if self.attributes[_key]:
                    _field_dict[_key] = self.attributes[_key].to_dict()
            _dict['attributes'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EntityDefinition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "relations": dict(
                (_k, RelationDefinition.from_dict(_v))
                for _k, _v in obj["relations"].items()
            )
            if obj.get("relations") is not None
            else None,
            "permissions": dict(
                (_k, PermissionDefinition.from_dict(_v))
                for _k, _v in obj["permissions"].items()
            )
            if obj.get("permissions") is not None
            else None,
            "attributes": dict(
                (_k, AttributeDefinition.from_dict(_v))
                for _k, _v in obj["attributes"].items()
            )
            if obj.get("attributes") is not None
            else None,
            "references": dict((_k, _v) for _k, _v in obj.get("references").items())
        })
        return _obj


