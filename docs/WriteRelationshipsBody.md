# WriteRelationshipsBody

Represents a request to write relationship data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**RelationshipWriteRequestMetadata**](RelationshipWriteRequestMetadata.md) |  | [optional] 
**tuples** | [**List[Tuple]**](Tuple.md) | List of tuples for the request. Must have between 1 and 100 items. | [optional] 

## Example

```python
from permify.models.write_relationships_body import WriteRelationshipsBody

# TODO update the JSON string below
json = "{}"
# create an instance of WriteRelationshipsBody from a JSON string
write_relationships_body_instance = WriteRelationshipsBody.from_json(json)
# print the JSON string representation of the object
print(WriteRelationshipsBody.to_json())

# convert the object into a dict
write_relationships_body_dict = write_relationships_body_instance.to_dict()
# create an instance of WriteRelationshipsBody from a dict
write_relationships_body_from_dict = WriteRelationshipsBody.from_dict(write_relationships_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


