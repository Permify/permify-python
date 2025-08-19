# SchemaPartialWriteRequestMetadata

SchemaPartialWriteRequestMetadata provides additional information for the Schema Partial Write request. It contains schema_version to specify which version of the schema should be read.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** | schema_version is the string that identifies the version of the schema to be read. | [optional] 

## Example

```python
from permify.models.schema_partial_write_request_metadata import SchemaPartialWriteRequestMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaPartialWriteRequestMetadata from a JSON string
schema_partial_write_request_metadata_instance = SchemaPartialWriteRequestMetadata.from_json(json)
# print the JSON string representation of the object
print SchemaPartialWriteRequestMetadata.to_json()

# convert the object into a dict
schema_partial_write_request_metadata_dict = schema_partial_write_request_metadata_instance.to_dict()
# create an instance of SchemaPartialWriteRequestMetadata from a dict
schema_partial_write_request_metadata_form_dict = schema_partial_write_request_metadata.from_dict(schema_partial_write_request_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


