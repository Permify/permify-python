# RelationshipDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**TupleFilter**](TupleFilter.md) |  | [optional] 

## Example

```python
from openapi_client.models.relationship_delete_request import RelationshipDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RelationshipDeleteRequest from a JSON string
relationship_delete_request_instance = RelationshipDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(RelationshipDeleteRequest.to_json())

# convert the object into a dict
relationship_delete_request_dict = relationship_delete_request_instance.to_dict()
# create an instance of RelationshipDeleteRequest from a dict
relationship_delete_request_form_dict = relationship_delete_request.from_dict(relationship_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


