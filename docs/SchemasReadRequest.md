# SchemasReadRequest

SchemaReadRequest is the request message for the Read method in the Schema service. It contains tenant_id and metadata about the schema to be read.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**SchemaReadRequestMetadata**](SchemaReadRequestMetadata.md) |  | [optional] 

## Example

```python
from openapi_client.models.schemas_read_request import SchemasReadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SchemasReadRequest from a JSON string
schemas_read_request_instance = SchemasReadRequest.from_json(json)
# print the JSON string representation of the object
print(SchemasReadRequest.to_json())

# convert the object into a dict
schemas_read_request_dict = schemas_read_request_instance.to_dict()
# create an instance of SchemasReadRequest from a dict
schemas_read_request_form_dict = schemas_read_request.from_dict(schemas_read_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


