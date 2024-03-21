# RelationshipDeleteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snap_token** | **str** | The snap token to avoid stale cache, see more details on [Snap Tokens](../../operations/snap-tokens) | [optional] 

## Example

```python
from permify.models.relationship_delete_response import RelationshipDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RelationshipDeleteResponse from a JSON string
relationship_delete_response_instance = RelationshipDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(RelationshipDeleteResponse.to_json())

# convert the object into a dict
relationship_delete_response_dict = relationship_delete_response_instance.to_dict()
# create an instance of RelationshipDeleteResponse from a dict
relationship_delete_response_form_dict = relationship_delete_response.from_dict(relationship_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


