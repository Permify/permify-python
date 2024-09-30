# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v1.1.2
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
from permify.models.constant import Constant
from permify.models.ident import Ident
from typing import Optional, Set
from typing_extensions import Self

class Expr(BaseModel):
    """
    An abstract representation of a common expression.  Expressions are abstractly represented as a collection of identifiers, select statements, function calls, literals, and comprehensions. All operators with the exception of the '.' operator are modelled as function calls. This makes it easy to represent new operators into the existing AST.  All references within expressions must resolve to a [Decl][google.api.expr.v1alpha1.Decl] provided at type-check for an expression to be valid. A reference may either be a bare identifier `name` or a qualified identifier `google.api.name`. References may either refer to a value or a function declaration.  For example, the expression `google.api.name.startsWith('expr')` references the declaration `google.api.name` within a [Expr.Select][google.api.expr.v1alpha1.Expr.Select] expression, and the function declaration `startsWith`.
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Required. An id assigned to this node by the parser which is unique in a given expression tree. This is used to associate type information and other attributes to a node in the parse tree.")
    const_expr: Optional[Constant] = Field(default=None, alias="constExpr")
    ident_expr: Optional[Ident] = Field(default=None, alias="identExpr")
    select_expr: Optional[Select] = Field(default=None, alias="selectExpr")
    call_expr: Optional[ExprCall] = Field(default=None, alias="callExpr")
    list_expr: Optional[CreateList] = Field(default=None, alias="listExpr")
    struct_expr: Optional[CreateStruct] = Field(default=None, alias="structExpr")
    comprehension_expr: Optional[Comprehension] = Field(default=None, alias="comprehensionExpr")
    __properties: ClassVar[List[str]] = ["id", "constExpr", "identExpr", "selectExpr", "callExpr", "listExpr", "structExpr", "comprehensionExpr"]

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
        """Create an instance of Expr from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of const_expr
        if self.const_expr:
            _dict['constExpr'] = self.const_expr.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ident_expr
        if self.ident_expr:
            _dict['identExpr'] = self.ident_expr.to_dict()
        # override the default output from pydantic by calling `to_dict()` of select_expr
        if self.select_expr:
            _dict['selectExpr'] = self.select_expr.to_dict()
        # override the default output from pydantic by calling `to_dict()` of call_expr
        if self.call_expr:
            _dict['callExpr'] = self.call_expr.to_dict()
        # override the default output from pydantic by calling `to_dict()` of list_expr
        if self.list_expr:
            _dict['listExpr'] = self.list_expr.to_dict()
        # override the default output from pydantic by calling `to_dict()` of struct_expr
        if self.struct_expr:
            _dict['structExpr'] = self.struct_expr.to_dict()
        # override the default output from pydantic by calling `to_dict()` of comprehension_expr
        if self.comprehension_expr:
            _dict['comprehensionExpr'] = self.comprehension_expr.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Expr from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "constExpr": Constant.from_dict(obj["constExpr"]) if obj.get("constExpr") is not None else None,
            "identExpr": Ident.from_dict(obj["identExpr"]) if obj.get("identExpr") is not None else None,
            "selectExpr": Select.from_dict(obj["selectExpr"]) if obj.get("selectExpr") is not None else None,
            "callExpr": ExprCall.from_dict(obj["callExpr"]) if obj.get("callExpr") is not None else None,
            "listExpr": CreateList.from_dict(obj["listExpr"]) if obj.get("listExpr") is not None else None,
            "structExpr": CreateStruct.from_dict(obj["structExpr"]) if obj.get("structExpr") is not None else None,
            "comprehensionExpr": Comprehension.from_dict(obj["comprehensionExpr"]) if obj.get("comprehensionExpr") is not None else None
        })
        return _obj

from permify.models.comprehension import Comprehension
from permify.models.create_list import CreateList
from permify.models.create_struct import CreateStruct
from permify.models.expr_call import ExprCall
from permify.models.select import Select
# TODO: Rewrite to not use raise_errors
Expr.model_rebuild(raise_errors=False)

