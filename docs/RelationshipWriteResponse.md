# RelationshipWriteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snap_token** | **str** | The snap token to avoid stale cache, see more details on [Snap Tokens](../../operations/snap-tokens) | [optional] 

## Example

```python
from permify.models.relationship_write_response import RelationshipWriteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RelationshipWriteResponse from a JSON string
relationship_write_response_instance = RelationshipWriteResponse.from_json(json)
# print the JSON string representation of the object
print(RelationshipWriteResponse.to_json())

# convert the object into a dict
relationship_write_response_dict = relationship_write_response_instance.to_dict()
# create an instance of RelationshipWriteResponse from a dict
relationship_write_response_from_dict = RelationshipWriteResponse.from_dict(relationship_write_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


