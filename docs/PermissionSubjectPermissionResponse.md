# PermissionSubjectPermissionResponse

PermissionSubjectPermissionResponse is the response message for the SubjectPermission method in the Permission service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**Dict[str, CheckResult]**](CheckResult.md) | Map of results for each permission check. | [optional] 

## Example

```python
from permify.models.permission_subject_permission_response import PermissionSubjectPermissionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionSubjectPermissionResponse from a JSON string
permission_subject_permission_response_instance = PermissionSubjectPermissionResponse.from_json(json)
# print the JSON string representation of the object
print(PermissionSubjectPermissionResponse.to_json())

# convert the object into a dict
permission_subject_permission_response_dict = permission_subject_permission_response_instance.to_dict()
# create an instance of PermissionSubjectPermissionResponse from a dict
permission_subject_permission_response_from_dict = PermissionSubjectPermissionResponse.from_dict(permission_subject_permission_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


