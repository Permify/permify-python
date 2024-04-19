# ExprCall

A call expression, including calls to predefined functions and operators.  For example, `value == 10`, `size(map_value)`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | [**Expr**](Expr.md) |  | [optional] 
**function** | **str** | Required. The name of the function or method being called. | [optional] 
**args** | [**List[Expr]**](Expr.md) | The arguments. | [optional] 

## Example

```python
from permify.models.expr_call import ExprCall

# TODO update the JSON string below
json = "{}"
# create an instance of ExprCall from a JSON string
expr_call_instance = ExprCall.from_json(json)
# print the JSON string representation of the object
print(ExprCall.to_json())

# convert the object into a dict
expr_call_dict = expr_call_instance.to_dict()
# create an instance of ExprCall from a dict
expr_call_from_dict = ExprCall.from_dict(expr_call_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


