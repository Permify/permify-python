# SchemasWriteRequest

SchemaWriteRequest is the request message for the Write method in the Schema service. It contains tenant_id and the schema to be written.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | schema is the string representation of the schema to be written. | [optional] 

## Example

```python
from openapi_client.models.schemas_write_request import SchemasWriteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SchemasWriteRequest from a JSON string
schemas_write_request_instance = SchemasWriteRequest.from_json(json)
# print the JSON string representation of the object
print(SchemasWriteRequest.to_json())

# convert the object into a dict
schemas_write_request_dict = schemas_write_request_instance.to_dict()
# create an instance of SchemasWriteRequest from a dict
schemas_write_request_form_dict = schemas_write_request.from_dict(schemas_write_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


