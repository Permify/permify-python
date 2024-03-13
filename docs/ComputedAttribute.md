# ComputedAttribute

ComputedAttribute defines a computed attribute which includes its name.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 

## Example

```python
from permify.models.computed_attribute import ComputedAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of ComputedAttribute from a JSON string
computed_attribute_instance = ComputedAttribute.from_json(json)
# print the JSON string representation of the object
print(ComputedAttribute.to_json())

# convert the object into a dict
computed_attribute_dict = computed_attribute_instance.to_dict()
# create an instance of ComputedAttribute from a dict
computed_attribute_form_dict = computed_attribute.from_dict(computed_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


