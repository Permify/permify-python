# RelationshipReadResponse

RelationshipReadResponse defines the structure of the response after reading relationships. It includes the tuples representing the relationships and a continuous token for handling result pagination.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tuples** | [**List[Tuple]**](Tuple.md) | tuples is a list of the relationships retrieved in the read operation, represented as entity-relation-entity triples. | [optional] 
**continuous_token** | **str** | continuous_token is used in the case of paginated reads to retrieve the next page of results. | [optional] 

## Example

```python
from permify.models.relationship_read_response import RelationshipReadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RelationshipReadResponse from a JSON string
relationship_read_response_instance = RelationshipReadResponse.from_json(json)
# print the JSON string representation of the object
print(RelationshipReadResponse.to_json())

# convert the object into a dict
relationship_read_response_dict = relationship_read_response_instance.to_dict()
# create an instance of RelationshipReadResponse from a dict
relationship_read_response_form_dict = relationship_read_response.from_dict(relationship_read_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


