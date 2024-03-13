# AttributeDefinition

The AttributeDefinition message provides detailed information about a specific attribute.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the attribute, which follows a specific string pattern and has a maximum byte size. | [optional] 
**type** | [**AttributeType**](AttributeType.md) |  | [optional] 

## Example

```python
from openapi_client.models.attribute_definition import AttributeDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeDefinition from a JSON string
attribute_definition_instance = AttributeDefinition.from_json(json)
# print the JSON string representation of the object
print(AttributeDefinition.to_json())

# convert the object into a dict
attribute_definition_dict = attribute_definition_instance.to_dict()
# create an instance of AttributeDefinition from a dict
attribute_definition_form_dict = attribute_definition.from_dict(attribute_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


