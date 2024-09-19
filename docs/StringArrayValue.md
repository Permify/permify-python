# StringArrayValue

Wrapper for an array of strings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[str]** | The array of strings. | [optional] 

## Example

```python
from permify.models.string_array_value import StringArrayValue

# TODO update the JSON string below
json = "{}"
# create an instance of StringArrayValue from a JSON string
string_array_value_instance = StringArrayValue.from_json(json)
# print the JSON string representation of the object
print(StringArrayValue.to_json())

# convert the object into a dict
string_array_value_dict = string_array_value_instance.to_dict()
# create an instance of StringArrayValue from a dict
string_array_value_from_dict = StringArrayValue.from_dict(string_array_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


