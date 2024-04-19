# EntityDefinition

The EntityDefinition message provides detailed information about a specific entity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the entity, which follows a specific string pattern and has a maximum byte size. | [optional] 
**relations** | [**Dict[str, RelationDefinition]**](RelationDefinition.md) | Map of relation definitions within this entity. The key is the relation name, and the value is the RelationDefinition. | [optional] 
**permissions** | [**Dict[str, PermissionDefinition]**](PermissionDefinition.md) | Map of permission definitions within this entity. The key is the permission name, and the value is the PermissionDefinition. | [optional] 
**attributes** | [**Dict[str, AttributeDefinition]**](AttributeDefinition.md) | Map of attribute definitions within this entity. The key is the attribute name, and the value is the AttributeDefinition. | [optional] 
**references** | [**Dict[str, EntityDefinitionReference]**](EntityDefinitionReference.md) | Map of references indicating whether a string pertains to a relation, permission, or attribute. | [optional] 

## Example

```python
from permify.models.entity_definition import EntityDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of EntityDefinition from a JSON string
entity_definition_instance = EntityDefinition.from_json(json)
# print the JSON string representation of the object
print(EntityDefinition.to_json())

# convert the object into a dict
entity_definition_dict = entity_definition_instance.to_dict()
# create an instance of EntityDefinition from a dict
entity_definition_from_dict = EntityDefinition.from_dict(entity_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


