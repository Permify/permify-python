# ContextAttribute

ContextAttribute defines a context attribute which includes its name.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 

## Example

```python
from permify.models.context_attribute import ContextAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of ContextAttribute from a JSON string
context_attribute_instance = ContextAttribute.from_json(json)
# print the JSON string representation of the object
print(ContextAttribute.to_json())

# convert the object into a dict
context_attribute_dict = context_attribute_instance.to_dict()
# create an instance of ContextAttribute from a dict
context_attribute_from_dict = ContextAttribute.from_dict(context_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


