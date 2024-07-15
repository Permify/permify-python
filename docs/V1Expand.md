# V1Expand

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
from permify.models.v1_expand import V1Expand

# TODO update the JSON string below
json = "{}"
# create an instance of V1Expand from a JSON string
v1_expand_instance = V1Expand.from_json(json)
# print the JSON string representation of the object
print(V1Expand.to_json())

# convert the object into a dict
v1_expand_dict = v1_expand_instance.to_dict()
# create an instance of V1Expand from a dict
v1_expand_from_dict = V1Expand.from_dict(v1_expand_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


