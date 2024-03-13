# RelationshipReadRequestMetadata

RelationshipReadRequestMetadata defines the structure of the metadata for a read request focused on relationships. It includes the snap_token associated with a particular state of the database.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snap_token** | **str** | snap_token represents a specific state or \&quot;snapshot\&quot; of the database. | [optional] 

## Example

```python
from permify.models.relationship_read_request_metadata import RelationshipReadRequestMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of RelationshipReadRequestMetadata from a JSON string
relationship_read_request_metadata_instance = RelationshipReadRequestMetadata.from_json(json)
# print the JSON string representation of the object
print(RelationshipReadRequestMetadata.to_json())

# convert the object into a dict
relationship_read_request_metadata_dict = relationship_read_request_metadata_instance.to_dict()
# create an instance of RelationshipReadRequestMetadata from a dict
relationship_read_request_metadata_form_dict = relationship_read_request_metadata.from_dict(relationship_read_request_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


