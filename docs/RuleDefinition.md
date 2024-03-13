# RuleDefinition

The RuleDefinition message provides detailed information about a specific rule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the rule, which follows a specific string pattern and has a maximum byte size. | [optional] 
**arguments** | [**Dict[str, AttributeType]**](AttributeType.md) | Map of arguments for this rule. The key is the attribute name, and the value is the AttributeType. | [optional] 
**expression** | [**CheckedExpr**](CheckedExpr.md) |  | [optional] 

## Example

```python
from permify.models.rule_definition import RuleDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of RuleDefinition from a JSON string
rule_definition_instance = RuleDefinition.from_json(json)
# print the JSON string representation of the object
print(RuleDefinition.to_json())

# convert the object into a dict
rule_definition_dict = rule_definition_instance.to_dict()
# create an instance of RuleDefinition from a dict
rule_definition_form_dict = rule_definition.from_dict(rule_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


