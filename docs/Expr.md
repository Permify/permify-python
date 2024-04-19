# Expr

An abstract representation of a common expression.  Expressions are abstractly represented as a collection of identifiers, select statements, function calls, literals, and comprehensions. All operators with the exception of the '.' operator are modelled as function calls. This makes it easy to represent new operators into the existing AST.  All references within expressions must resolve to a [Decl][google.api.expr.v1alpha1.Decl] provided at type-check for an expression to be valid. A reference may either be a bare identifier `name` or a qualified identifier `google.api.name`. References may either refer to a value or a function declaration.  For example, the expression `google.api.name.startsWith('expr')` references the declaration `google.api.name` within a [Expr.Select][google.api.expr.v1alpha1.Expr.Select] expression, and the function declaration `startsWith`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Required. An id assigned to this node by the parser which is unique in a given expression tree. This is used to associate type information and other attributes to a node in the parse tree. | [optional] 
**const_expr** | [**Constant**](Constant.md) |  | [optional] 
**ident_expr** | [**Ident**](Ident.md) |  | [optional] 
**select_expr** | [**Select**](Select.md) |  | [optional] 
**call_expr** | [**ExprCall**](ExprCall.md) |  | [optional] 
**list_expr** | [**CreateList**](CreateList.md) |  | [optional] 
**struct_expr** | [**CreateStruct**](CreateStruct.md) |  | [optional] 
**comprehension_expr** | [**Comprehension**](Comprehension.md) |  | [optional] 

## Example

```python
from permify.models.expr import Expr

# TODO update the JSON string below
json = "{}"
# create an instance of Expr from a JSON string
expr_instance = Expr.from_json(json)
# print the JSON string representation of the object
print(Expr.to_json())

# convert the object into a dict
expr_dict = expr_instance.to_dict()
# create an instance of Expr from a dict
expr_from_dict = Expr.from_dict(expr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


