# PermissionsSubjectPermissionRequest

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
from openapi_client.models.permissions_subject_permission_request import PermissionsSubjectPermissionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionsSubjectPermissionRequest from a JSON string
permissions_subject_permission_request_instance = PermissionsSubjectPermissionRequest.from_json(json)
# print the JSON string representation of the object
print(PermissionsSubjectPermissionRequest.to_json())

# convert the object into a dict
permissions_subject_permission_request_dict = permissions_subject_permission_request_instance.to_dict()
# create an instance of PermissionsSubjectPermissionRequest from a dict
permissions_subject_permission_request_form_dict = permissions_subject_permission_request.from_dict(permissions_subject_permission_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


