# SchemaReadBody

SchemaReadRequest is the request message for the Read method in the Schema service. It contains tenant_id and metadata about the schema to be read.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**SchemaReadRequestMetadata**](SchemaReadRequestMetadata.md) |  | [optional] 

## Example

```python
from permify.models.schema_read_body import SchemaReadBody

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaReadBody from a JSON string
schema_read_body_instance = SchemaReadBody.from_json(json)
# print the JSON string representation of the object
print SchemaReadBody.to_json()

# convert the object into a dict
schema_read_body_dict = schema_read_body_instance.to_dict()
# create an instance of SchemaReadBody from a dict
schema_read_body_form_dict = schema_read_body.from_dict(schema_read_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


