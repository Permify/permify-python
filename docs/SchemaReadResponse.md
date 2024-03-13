# SchemaReadResponse

SchemaReadResponse is the response message for the Read method in the Schema service. It returns the requested schema.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**SchemaDefinition**](SchemaDefinition.md) |  | [optional] 

## Example

```python
from openapi_client.models.schema_read_response import SchemaReadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaReadResponse from a JSON string
schema_read_response_instance = SchemaReadResponse.from_json(json)
# print the JSON string representation of the object
print(SchemaReadResponse.to_json())

# convert the object into a dict
schema_read_response_dict = schema_read_response_instance.to_dict()
# create an instance of SchemaReadResponse from a dict
schema_read_response_form_dict = schema_read_response.from_dict(schema_read_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


