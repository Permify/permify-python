# FunctionType

Function type with result and arg types.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_type** | [**V1alpha1Type**](V1alpha1Type.md) |  | [optional] 
**arg_types** | [**List[V1alpha1Type]**](V1alpha1Type.md) | Argument types of the function. | [optional] 

## Example

```python
from openapi_client.models.function_type import FunctionType

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionType from a JSON string
function_type_instance = FunctionType.from_json(json)
# print the JSON string representation of the object
print(FunctionType.to_json())

# convert the object into a dict
function_type_dict = function_type_instance.to_dict()
# create an instance of FunctionType from a dict
function_type_form_dict = function_type.from_dict(function_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


