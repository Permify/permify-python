# DataWriteRequestMetadata

DataWriteRequestMetadata defines the structure of metadata for a write request. It includes the schema version of the data to be written.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** | schema_version represents the version of the schema for the data being written. | [optional] 

## Example

```python
from permify.models.data_write_request_metadata import DataWriteRequestMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of DataWriteRequestMetadata from a JSON string
data_write_request_metadata_instance = DataWriteRequestMetadata.from_json(json)
# print the JSON string representation of the object
print(DataWriteRequestMetadata.to_json())

# convert the object into a dict
data_write_request_metadata_dict = data_write_request_metadata_instance.to_dict()
# create an instance of DataWriteRequestMetadata from a dict
data_write_request_metadata_from_dict = DataWriteRequestMetadata.from_dict(data_write_request_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


