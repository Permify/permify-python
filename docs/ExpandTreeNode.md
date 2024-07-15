# ExpandTreeNode

ExpandTreeNode represents a node in an expansion tree with a specific operation and its children.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | [**ExpandTreeNodeOperation**](ExpandTreeNodeOperation.md) |  | [optional] 
**children** | [**List[Expand]**](Expand.md) |  | [optional] 

## Example

```python
from permify.models.expand_tree_node import ExpandTreeNode

# TODO update the JSON string below
json = "{}"
# create an instance of ExpandTreeNode from a JSON string
expand_tree_node_instance = ExpandTreeNode.from_json(json)
# print the JSON string representation of the object
print(ExpandTreeNode.to_json())

# convert the object into a dict
expand_tree_node_dict = expand_tree_node_instance.to_dict()
# create an instance of ExpandTreeNode from a dict
expand_tree_node_from_dict = ExpandTreeNode.from_dict(expand_tree_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


