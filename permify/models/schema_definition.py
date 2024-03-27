# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v0.7.9
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
from permify.models.entity_definition import EntityDefinition
from permify.models.rule_definition import RuleDefinition
from permify.models.schema_definition_reference import SchemaDefinitionReference
from typing import Optional, Set
from typing_extensions import Self

class SchemaDefinition(BaseModel):
    """
    The SchemaDefinition message provides definitions for entities and rules, and includes references to clarify whether a name refers to an entity or a rule.
    """ # noqa: E501
    entity_definitions: Optional[Dict[str, EntityDefinition]] = Field(default=None, description="Map of entity definitions. The key is the entity name, and the value is the corresponding EntityDefinition.", alias="entityDefinitions")
    rule_definitions: Optional[Dict[str, RuleDefinition]] = Field(default=None, description="Map of rule definitions. The key is the rule name, and the value is the corresponding RuleDefinition.", alias="ruleDefinitions")
    references: Optional[Dict[str, SchemaDefinitionReference]] = Field(default=None, description="Map of references to signify whether a string refers to an entity or a rule.")
    __properties: ClassVar[List[str]] = ["entityDefinitions", "ruleDefinitions", "references"]

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
        """Create an instance of SchemaDefinition from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in entity_definitions (dict)
        _field_dict = {}
        if self.entity_definitions:
            for _key in self.entity_definitions:
                if self.entity_definitions[_key]:
                    _field_dict[_key] = self.entity_definitions[_key].to_dict()
            _dict['entityDefinitions'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in rule_definitions (dict)
        _field_dict = {}
        if self.rule_definitions:
            for _key in self.rule_definitions:
                if self.rule_definitions[_key]:
                    _field_dict[_key] = self.rule_definitions[_key].to_dict()
            _dict['ruleDefinitions'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SchemaDefinition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "entityDefinitions": dict(
                (_k, EntityDefinition.from_dict(_v))
                for _k, _v in obj["entityDefinitions"].items()
            )
            if obj.get("entityDefinitions") is not None
            else None,
            "ruleDefinitions": dict(
                (_k, RuleDefinition.from_dict(_v))
                for _k, _v in obj["ruleDefinitions"].items()
            )
            if obj.get("ruleDefinitions") is not None
            else None,
            "references": dict((_k, _v) for _k, _v in obj.get("references").items())
        })
        return _obj


