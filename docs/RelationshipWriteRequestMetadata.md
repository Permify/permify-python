# RelationshipWriteRequestMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 

## Example

```python
from permify.models.relationship_write_request_metadata import RelationshipWriteRequestMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of RelationshipWriteRequestMetadata from a JSON string
relationship_write_request_metadata_instance = RelationshipWriteRequestMetadata.from_json(json)
# print the JSON string representation of the object
print(RelationshipWriteRequestMetadata.to_json())

# convert the object into a dict
relationship_write_request_metadata_dict = relationship_write_request_metadata_instance.to_dict()
# create an instance of RelationshipWriteRequestMetadata from a dict
relationship_write_request_metadata_from_dict = RelationshipWriteRequestMetadata.from_dict(relationship_write_request_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


