# TupleFilter

TupleFilter is used to filter tuples based on the entity, relation and the subject.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**EntityFilter**](EntityFilter.md) |  | [optional] 
**relation** | **str** |  | [optional] 
**subject** | [**SubjectFilter**](SubjectFilter.md) |  | [optional] 

## Example

```python
from permify.models.tuple_filter import TupleFilter

# TODO update the JSON string below
json = "{}"
# create an instance of TupleFilter from a JSON string
tuple_filter_instance = TupleFilter.from_json(json)
# print the JSON string representation of the object
print TupleFilter.to_json()

# convert the object into a dict
tuple_filter_dict = tuple_filter_instance.to_dict()
# create an instance of TupleFilter from a dict
tuple_filter_form_dict = tuple_filter.from_dict(tuple_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


