# TupleSet

TupleSet represents a set of tuples associated with a specific relation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relation** | **str** |  | [optional] 

## Example

```python
from permify.models.tuple_set import TupleSet

# TODO update the JSON string below
json = "{}"
# create an instance of TupleSet from a JSON string
tuple_set_instance = TupleSet.from_json(json)
# print the JSON string representation of the object
print(TupleSet.to_json())

# convert the object into a dict
tuple_set_dict = tuple_set_instance.to_dict()
# create an instance of TupleSet from a dict
tuple_set_from_dict = TupleSet.from_dict(tuple_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


