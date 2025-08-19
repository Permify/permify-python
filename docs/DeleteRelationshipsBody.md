# DeleteRelationshipsBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**TupleFilter**](TupleFilter.md) |  | [optional] 

## Example

```python
from permify.models.delete_relationships_body import DeleteRelationshipsBody

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteRelationshipsBody from a JSON string
delete_relationships_body_instance = DeleteRelationshipsBody.from_json(json)
# print the JSON string representation of the object
print DeleteRelationshipsBody.to_json()

# convert the object into a dict
delete_relationships_body_dict = delete_relationships_body_instance.to_dict()
# create an instance of DeleteRelationshipsBody from a dict
delete_relationships_body_form_dict = delete_relationships_body.from_dict(delete_relationships_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


