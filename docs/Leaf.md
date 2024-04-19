# Leaf

Leaf represents a leaf node in the permission tree.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**computed_user_set** | [**ComputedUserSet**](ComputedUserSet.md) |  | [optional] 
**tuple_to_user_set** | [**TupleToUserSet**](TupleToUserSet.md) |  | [optional] 
**computed_attribute** | [**ComputedAttribute**](ComputedAttribute.md) |  | [optional] 
**call** | [**V1Call**](V1Call.md) |  | [optional] 

## Example

```python
from permify.models.leaf import Leaf

# TODO update the JSON string below
json = "{}"
# create an instance of Leaf from a JSON string
leaf_instance = Leaf.from_json(json)
# print the JSON string representation of the object
print(Leaf.to_json())

# convert the object into a dict
leaf_dict = leaf_instance.to_dict()
# create an instance of Leaf from a dict
leaf_from_dict = Leaf.from_dict(leaf_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


