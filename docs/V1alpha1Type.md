# V1alpha1Type

Represents a CEL type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dyn** | **object** | Dynamic type. | [optional] 
**null** | **str** | Null value. | [optional] 
**primitive** | [**PrimitiveType**](PrimitiveType.md) |  | [optional] 
**wrapper** | [**PrimitiveType**](PrimitiveType.md) |  | [optional] 
**well_known** | [**WellKnownType**](WellKnownType.md) |  | [optional] 
**list_type** | [**ListType**](ListType.md) |  | [optional] 
**map_type** | [**MapType**](MapType.md) |  | [optional] 
**function** | [**FunctionType**](FunctionType.md) |  | [optional] 
**message_type** | **str** | Protocol buffer message type.  The &#x60;message_type&#x60; string specifies the qualified message type name. For example, &#x60;google.plus.Profile&#x60;. | [optional] 
**type_param** | **str** | Type param type.  The &#x60;type_param&#x60; string specifies the type parameter name, e.g. &#x60;list&lt;E&gt;&#x60; would be a &#x60;list_type&#x60; whose element type was a &#x60;type_param&#x60; type named &#x60;E&#x60;. | [optional] 
**type** | [**V1alpha1Type**](V1alpha1Type.md) |  | [optional] 
**error** | **object** | Error type.  During type-checking if an expression is an error, its type is propagated as the &#x60;ERROR&#x60; type. This permits the type-checker to discover other errors present in the expression. | [optional] 
**abstract_type** | [**AbstractType**](AbstractType.md) |  | [optional] 

## Example

```python
from permify.models.v1alpha1_type import V1alpha1Type

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1Type from a JSON string
v1alpha1_type_instance = V1alpha1Type.from_json(json)
# print the JSON string representation of the object
print(V1alpha1Type.to_json())

# convert the object into a dict
v1alpha1_type_dict = v1alpha1_type_instance.to_dict()
# create an instance of V1alpha1Type from a dict
v1alpha1_type_form_dict = v1alpha1_type.from_dict(v1alpha1_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


