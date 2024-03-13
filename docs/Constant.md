# Constant

Represents a primitive literal.  Named 'Constant' here for backwards compatibility.  This is similar as the primitives supported in the well-known type `google.protobuf.Value`, but richer so it can represent CEL's full range of primitives.  Lists and structs are not included as constants as these aggregate types may contain [Expr][google.api.expr.v1alpha1.Expr] elements which require evaluation and are thus not constant.  Examples of literals include: `\"hello\"`, `b'bytes'`, `1u`, `4.2`, `-2`, `true`, `null`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**null_value** | **str** | null value. | [optional] 
**bool_value** | **bool** | boolean value. | [optional] 
**int64_value** | **str** | int64 value. | [optional] 
**uint64_value** | **str** | uint64 value. | [optional] 
**double_value** | **float** | double value. | [optional] 
**string_value** | **str** | string value. | [optional] 
**bytes_value** | **bytearray** | bytes value. | [optional] 
**duration_value** | **str** | protobuf.Duration value.  Deprecated: duration is no longer considered a builtin cel type. | [optional] 
**timestamp_value** | **datetime** | protobuf.Timestamp value.  Deprecated: timestamp is no longer considered a builtin cel type. | [optional] 

## Example

```python
from openapi_client.models.constant import Constant

# TODO update the JSON string below
json = "{}"
# create an instance of Constant from a JSON string
constant_instance = Constant.from_json(json)
# print the JSON string representation of the object
print(Constant.to_json())

# convert the object into a dict
constant_dict = constant_instance.to_dict()
# create an instance of Constant from a dict
constant_form_dict = constant.from_dict(constant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


