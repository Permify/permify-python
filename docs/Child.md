# Child

Child represents a node in the permission tree.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**leaf** | [**Leaf**](Leaf.md) |  | [optional] 
**rewrite** | [**Rewrite**](Rewrite.md) |  | [optional] 

## Example

```python
from permify.models.child import Child

# TODO update the JSON string below
json = "{}"
# create an instance of Child from a JSON string
child_instance = Child.from_json(json)
# print the JSON string representation of the object
print(Child.to_json())

# convert the object into a dict
child_dict = child_instance.to_dict()
# create an instance of Child from a dict
child_form_dict = child.from_dict(child_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


