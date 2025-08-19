# SubjectFilter

SubjectFilter is used to filter subjects based on the type, ids and relation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**ids** | **List[str]** |  | [optional] 
**relation** | **str** |  | [optional] 

## Example

```python
from permify.models.subject_filter import SubjectFilter

# TODO update the JSON string below
json = "{}"
# create an instance of SubjectFilter from a JSON string
subject_filter_instance = SubjectFilter.from_json(json)
# print the JSON string representation of the object
print SubjectFilter.to_json()

# convert the object into a dict
subject_filter_dict = subject_filter_instance.to_dict()
# create an instance of SubjectFilter from a dict
subject_filter_form_dict = subject_filter.from_dict(subject_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


