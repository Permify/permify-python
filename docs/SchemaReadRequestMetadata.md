# SchemaReadRequestMetadata

SchemaReadRequestMetadata provides additional information for the Schema Read request. It contains schema_version to specify which version of the schema should be read.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** | schema_version is the string that identifies the version of the schema to be read. | [optional] 

## Example

```python
from permify.models.schema_read_request_metadata import SchemaReadRequestMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaReadRequestMetadata from a JSON string
schema_read_request_metadata_instance = SchemaReadRequestMetadata.from_json(json)
# print the JSON string representation of the object
print(SchemaReadRequestMetadata.to_json())

# convert the object into a dict
schema_read_request_metadata_dict = schema_read_request_metadata_instance.to_dict()
# create an instance of SchemaReadRequestMetadata from a dict
schema_read_request_metadata_from_dict = SchemaReadRequestMetadata.from_dict(schema_read_request_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


