# PermissionsLookupSubjectRequest

PermissionLookupSubjectRequest is the request message for the LookupSubject method in the Permission service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**PermissionLookupSubjectRequestMetadata**](PermissionLookupSubjectRequestMetadata.md) |  | [optional] 
**entity** | [**Entity**](Entity.md) |  | [optional] 
**permission** | **str** | Permission to be checked, can be a permission or relation. Required, and must match the pattern \&quot;^([a-zA-Z][a-zA-Z0-9_]{1,62}[a-zA-Z0-9])$\&quot;, max 64 bytes. | [optional] 
**subject_reference** | [**RelationReference**](RelationReference.md) |  | [optional] 
**context** | [**Context**](Context.md) |  | [optional] 

## Example

```python
from permify.models.permissions_lookup_subject_request import PermissionsLookupSubjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionsLookupSubjectRequest from a JSON string
permissions_lookup_subject_request_instance = PermissionsLookupSubjectRequest.from_json(json)
# print the JSON string representation of the object
print(PermissionsLookupSubjectRequest.to_json())

# convert the object into a dict
permissions_lookup_subject_request_dict = permissions_lookup_subject_request_instance.to_dict()
# create an instance of PermissionsLookupSubjectRequest from a dict
permissions_lookup_subject_request_form_dict = permissions_lookup_subject_request.from_dict(permissions_lookup_subject_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


