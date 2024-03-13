# RelationDefinition

The RelationDefinition message provides detailed information about a specific relation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the relation, which follows a specific string pattern and has a maximum byte size. | [optional] 
**relation_references** | [**List[RelationReference]**](RelationReference.md) | A list of references to other relations. | [optional] 

## Example

```python
from openapi_client.models.relation_definition import RelationDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of RelationDefinition from a JSON string
relation_definition_instance = RelationDefinition.from_json(json)
# print the JSON string representation of the object
print(RelationDefinition.to_json())

# convert the object into a dict
relation_definition_dict = relation_definition_instance.to_dict()
# create an instance of RelationDefinition from a dict
relation_definition_form_dict = relation_definition.from_dict(relation_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


