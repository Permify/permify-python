# SchemaWriteResponse

SchemaWriteResponse is the response message for the Write method in the Schema service. It returns the version of the written schema.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** | schema_version is the string that identifies the version of the written schema. | [optional] 

## Example

```python
from permify.models.schema_write_response import SchemaWriteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaWriteResponse from a JSON string
schema_write_response_instance = SchemaWriteResponse.from_json(json)
# print the JSON string representation of the object
print(SchemaWriteResponse.to_json())

# convert the object into a dict
schema_write_response_dict = schema_write_response_instance.to_dict()
# create an instance of SchemaWriteResponse from a dict
schema_write_response_form_dict = schema_write_response.from_dict(schema_write_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


