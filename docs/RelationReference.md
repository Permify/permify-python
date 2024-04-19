# RelationReference

The RelationReference message provides a reference to a specific relation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the referenced entity, which follows a specific string pattern and has a maximum byte size. | [optional] 
**relation** | **str** | The name of the referenced relation, which follows a specific string pattern and has a maximum byte size. | [optional] 

## Example

```python
from permify.models.relation_reference import RelationReference

# TODO update the JSON string below
json = "{}"
# create an instance of RelationReference from a JSON string
relation_reference_instance = RelationReference.from_json(json)
# print the JSON string representation of the object
print(RelationReference.to_json())

# convert the object into a dict
relation_reference_dict = relation_reference_instance.to_dict()
# create an instance of RelationReference from a dict
relation_reference_from_dict = RelationReference.from_dict(relation_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


