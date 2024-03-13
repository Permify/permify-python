# PermissionsExpandRequest

PermissionExpandRequest is the request message for the Expand method in the Permission service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**PermissionExpandRequestMetadata**](PermissionExpandRequestMetadata.md) |  | [optional] 
**entity** | [**Entity**](Entity.md) |  | [optional] 
**permission** | **str** | Name of the permission to be expanded, not required, must start with a letter and can include alphanumeric and underscore, max 64 bytes. | [optional] 
**context** | [**Context**](Context.md) |  | [optional] 
**arguments** | [**List[Argument]**](Argument.md) | Additional arguments associated with this request. | [optional] 

## Example

```python
from permify.models.permissions_expand_request import PermissionsExpandRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionsExpandRequest from a JSON string
permissions_expand_request_instance = PermissionsExpandRequest.from_json(json)
# print the JSON string representation of the object
print(PermissionsExpandRequest.to_json())

# convert the object into a dict
permissions_expand_request_dict = permissions_expand_request_instance.to_dict()
# create an instance of PermissionsExpandRequest from a dict
permissions_expand_request_form_dict = permissions_expand_request.from_dict(permissions_expand_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


