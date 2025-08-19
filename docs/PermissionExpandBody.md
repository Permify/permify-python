# PermissionExpandBody

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
from permify.models.permission_expand_body import PermissionExpandBody

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionExpandBody from a JSON string
permission_expand_body_instance = PermissionExpandBody.from_json(json)
# print the JSON string representation of the object
print PermissionExpandBody.to_json()

# convert the object into a dict
permission_expand_body_dict = permission_expand_body_instance.to_dict()
# create an instance of PermissionExpandBody from a dict
permission_expand_body_form_dict = permission_expand_body.from_dict(permission_expand_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


