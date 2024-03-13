# ExpandLeaf

ExpandLeaf is the leaf node of an Expand tree and can be either a set of Subjects or a set of Values.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subjects** | [**Subjects**](Subjects.md) |  | [optional] 
**values** | [**Values**](Values.md) |  | [optional] 
**value** | [**Any**](Any.md) |  | [optional] 

## Example

```python
from openapi_client.models.expand_leaf import ExpandLeaf

# TODO update the JSON string below
json = "{}"
# create an instance of ExpandLeaf from a JSON string
expand_leaf_instance = ExpandLeaf.from_json(json)
# print the JSON string representation of the object
print(ExpandLeaf.to_json())

# convert the object into a dict
expand_leaf_dict = expand_leaf_instance.to_dict()
# create an instance of ExpandLeaf from a dict
expand_leaf_form_dict = expand_leaf.from_dict(expand_leaf_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


