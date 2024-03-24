# SchemaPartialWriteResponse

SchemaPartialWriteResponse is the response message for the Parietal Write method in the Schema service. It returns the requested schema.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** | schema_version is the string that identifies the version of the written schema. | [optional] 

## Example

```python
from permify.models.schema_partial_write_response import SchemaPartialWriteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaPartialWriteResponse from a JSON string
schema_partial_write_response_instance = SchemaPartialWriteResponse.from_json(json)
# print the JSON string representation of the object
print(SchemaPartialWriteResponse.to_json())

# convert the object into a dict
schema_partial_write_response_dict = schema_partial_write_response_instance.to_dict()
# create an instance of SchemaPartialWriteResponse from a dict
schema_partial_write_response_form_dict = schema_partial_write_response.from_dict(schema_partial_write_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


