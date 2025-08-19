# Subjects

Subjects holds a repeated field of Subject type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subjects** | [**List[Subject]**](Subject.md) | A list of subjects. | [optional] 

## Example

```python
from permify.models.subjects import Subjects

# TODO update the JSON string below
json = "{}"
# create an instance of Subjects from a JSON string
subjects_instance = Subjects.from_json(json)
# print the JSON string representation of the object
print Subjects.to_json()

# convert the object into a dict
subjects_dict = subjects_instance.to_dict()
# create an instance of Subjects from a dict
subjects_form_dict = subjects.from_dict(subjects_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


