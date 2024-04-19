# PermissionLookupSubjectResponse

PermissionLookupSubjectResponse is the response message for the LookupSubject method in the Permission service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject_ids** | **List[str]** | List of identifiers for subjects that match the lookup. | [optional] 

## Example

```python
from permify.models.permission_lookup_subject_response import PermissionLookupSubjectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionLookupSubjectResponse from a JSON string
permission_lookup_subject_response_instance = PermissionLookupSubjectResponse.from_json(json)
# print the JSON string representation of the object
print(PermissionLookupSubjectResponse.to_json())

# convert the object into a dict
permission_lookup_subject_response_dict = permission_lookup_subject_response_instance.to_dict()
# create an instance of PermissionLookupSubjectResponse from a dict
permission_lookup_subject_response_from_dict = PermissionLookupSubjectResponse.from_dict(permission_lookup_subject_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


