# Tuple

Tuple is a structure that includes an entity, a relation, and a subject.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**Entity**](Entity.md) |  | [optional] 
**relation** | **str** |  | [optional] 
**subject** | [**Subject**](Subject.md) |  | [optional] 

## Example

```python
from permify.models.tuple import Tuple

# TODO update the JSON string below
json = "{}"
# create an instance of Tuple from a JSON string
tuple_instance = Tuple.from_json(json)
# print the JSON string representation of the object
print(Tuple.to_json())

# convert the object into a dict
tuple_dict = tuple_instance.to_dict()
# create an instance of Tuple from a dict
tuple_from_dict = Tuple.from_dict(tuple_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


