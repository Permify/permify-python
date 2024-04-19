# SchemaDefinition

The SchemaDefinition message provides definitions for entities and rules, and includes references to clarify whether a name refers to an entity or a rule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_definitions** | [**Dict[str, EntityDefinition]**](EntityDefinition.md) | Map of entity definitions. The key is the entity name, and the value is the corresponding EntityDefinition. | [optional] 
**rule_definitions** | [**Dict[str, RuleDefinition]**](RuleDefinition.md) | Map of rule definitions. The key is the rule name, and the value is the corresponding RuleDefinition. | [optional] 
**references** | [**Dict[str, SchemaDefinitionReference]**](SchemaDefinitionReference.md) | Map of references to signify whether a string refers to an entity or a rule. | [optional] 

## Example

```python
from permify.models.schema_definition import SchemaDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaDefinition from a JSON string
schema_definition_instance = SchemaDefinition.from_json(json)
# print the JSON string representation of the object
print(SchemaDefinition.to_json())

# convert the object into a dict
schema_definition_dict = schema_definition_instance.to_dict()
# create an instance of SchemaDefinition from a dict
schema_definition_from_dict = SchemaDefinition.from_dict(schema_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


