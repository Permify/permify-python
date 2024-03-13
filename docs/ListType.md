# ListType

List type with typed elements, e.g. `list<example.proto.MyMessage>`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elem_type** | [**V1alpha1Type**](V1alpha1Type.md) |  | [optional] 

## Example

```python
from openapi_client.models.list_type import ListType

# TODO update the JSON string below
json = "{}"
# create an instance of ListType from a JSON string
list_type_instance = ListType.from_json(json)
# print the JSON string representation of the object
print(ListType.to_json())

# convert the object into a dict
list_type_dict = list_type_instance.to_dict()
# create an instance of ListType from a dict
list_type_form_dict = list_type.from_dict(list_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


