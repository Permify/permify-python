# Argument

Argument defines the type of argument in a Call. It can be either a ComputedAttribute or a ContextAttribute.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**computed_attribute** | [**ComputedAttribute**](ComputedAttribute.md) |  | [optional] 

## Example

```python
from permify.models.argument import Argument

# TODO update the JSON string below
json = "{}"
# create an instance of Argument from a JSON string
argument_instance = Argument.from_json(json)
# print the JSON string representation of the object
print(Argument.to_json())

# convert the object into a dict
argument_dict = argument_instance.to_dict()
# create an instance of Argument from a dict
argument_from_dict = Argument.from_dict(argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


