# CreateStruct

A map or message creation expression.  Maps are constructed as `{'key_name': 'value'}`. Message construction is similar, but prefixed with a type name and composed of field ids: `types.MyType{field_id: 'value'}`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_name** | **str** | The type name of the message to be created, empty when creating map literals. | [optional] 
**entries** | [**List[Entry]**](Entry.md) | The entries in the creation expression. | [optional] 

## Example

```python
from permify.models.create_struct import CreateStruct

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStruct from a JSON string
create_struct_instance = CreateStruct.from_json(json)
# print the JSON string representation of the object
print CreateStruct.to_json()

# convert the object into a dict
create_struct_dict = create_struct_instance.to_dict()
# create an instance of CreateStruct from a dict
create_struct_form_dict = create_struct.from_dict(create_struct_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


