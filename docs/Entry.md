# Entry

Represents an entry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Required. An id assigned to this node by the parser which is unique in a given expression tree. This is used to associate type information and other attributes to the node. | [optional] 
**field_key** | **str** | The field key for a message creator statement. | [optional] 
**map_key** | [**Expr**](Expr.md) |  | [optional] 
**value** | [**Expr**](Expr.md) |  | [optional] 
**optional_entry** | **bool** | Whether the key-value pair is optional. | [optional] 

## Example

```python
from permify.models.entry import Entry

# TODO update the JSON string below
json = "{}"
# create an instance of Entry from a JSON string
entry_instance = Entry.from_json(json)
# print the JSON string representation of the object
print(Entry.to_json())

# convert the object into a dict
entry_dict = entry_instance.to_dict()
# create an instance of Entry from a dict
entry_from_dict = Entry.from_dict(entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


