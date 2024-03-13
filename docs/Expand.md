# Expand

Expand is used to define a hierarchical structure for permissions. It has an entity, permission, and arguments. The node can be either another hierarchical structure or a set of subjects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**Entity**](Entity.md) |  | [optional] 
**permission** | **str** | permission is the permission applied to the entity. | [optional] 
**arguments** | [**List[Argument]**](Argument.md) | arguments are the additional information or context used to evaluate permissions. | [optional] 
**expand** | [**ExpandTreeNode**](ExpandTreeNode.md) |  | [optional] 
**leaf** | [**ExpandLeaf**](ExpandLeaf.md) |  | [optional] 

## Example

```python
from openapi_client.models.expand import Expand

# TODO update the JSON string below
json = "{}"
# create an instance of Expand from a JSON string
expand_instance = Expand.from_json(json)
# print the JSON string representation of the object
print(Expand.to_json())

# convert the object into a dict
expand_dict = expand_instance.to_dict()
# create an instance of Expand from a dict
expand_form_dict = expand.from_dict(expand_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


