# RelationshipsWriteRequest

Represents a request to write relationship data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**RelationshipWriteRequestMetadata**](RelationshipWriteRequestMetadata.md) |  | [optional] 
**tuples** | [**List[Tuple]**](Tuple.md) | List of tuples for the request. Must have between 1 and 100 items. | [optional] 

## Example

```python
from permify.models.relationships_write_request import RelationshipsWriteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RelationshipsWriteRequest from a JSON string
relationships_write_request_instance = RelationshipsWriteRequest.from_json(json)
# print the JSON string representation of the object
print(RelationshipsWriteRequest.to_json())

# convert the object into a dict
relationships_write_request_dict = relationships_write_request_instance.to_dict()
# create an instance of RelationshipsWriteRequest from a dict
relationships_write_request_from_dict = RelationshipsWriteRequest.from_dict(relationships_write_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


