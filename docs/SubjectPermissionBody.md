# SubjectPermissionBody

PermissionSubjectPermissionRequest is the request message for the SubjectPermission method in the Permission service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**PermissionSubjectPermissionRequestMetadata**](PermissionSubjectPermissionRequestMetadata.md) |  | [optional] 
**entity** | [**Entity**](Entity.md) |  | [optional] 
**subject** | [**Subject**](Subject.md) |  | [optional] 
**context** | [**Context**](Context.md) |  | [optional] 

## Example

```python
from permify.models.subject_permission_body import SubjectPermissionBody

# TODO update the JSON string below
json = "{}"
# create an instance of SubjectPermissionBody from a JSON string
subject_permission_body_instance = SubjectPermissionBody.from_json(json)
# print the JSON string representation of the object
print SubjectPermissionBody.to_json()

# convert the object into a dict
subject_permission_body_dict = subject_permission_body_instance.to_dict()
# create an instance of SubjectPermissionBody from a dict
subject_permission_body_form_dict = subject_permission_body.from_dict(subject_permission_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


