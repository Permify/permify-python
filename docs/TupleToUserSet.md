# TupleToUserSet

TupleToUserSet defines a mapping from tuple sets to computed user sets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tuple_set** | [**TupleSet**](TupleSet.md) |  | [optional] 
**computed** | [**ComputedUserSet**](ComputedUserSet.md) |  | [optional] 

## Example

```python
from permify.models.tuple_to_user_set import TupleToUserSet

# TODO update the JSON string below
json = "{}"
# create an instance of TupleToUserSet from a JSON string
tuple_to_user_set_instance = TupleToUserSet.from_json(json)
# print the JSON string representation of the object
print(TupleToUserSet.to_json())

# convert the object into a dict
tuple_to_user_set_dict = tuple_to_user_set_instance.to_dict()
# create an instance of TupleToUserSet from a dict
tuple_to_user_set_from_dict = TupleToUserSet.from_dict(tuple_to_user_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


