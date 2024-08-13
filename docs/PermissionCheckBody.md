# PermissionCheckBody

PermissionCheckRequest is the request message for the Check method in the Permission service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**PermissionCheckRequestMetadata**](PermissionCheckRequestMetadata.md) |  | [optional] 
**entity** | [**Entity**](Entity.md) |  | [optional] 
**permission** | **str** | The action the user wants to perform on the resource | [optional] 
**subject** | [**Subject**](Subject.md) |  | [optional] 
**context** | [**Context**](Context.md) |  | [optional] 
**arguments** | [**List[Argument]**](Argument.md) | Additional arguments associated with this request. | [optional] 

## Example

```python
from permify.models.permission_check_body import PermissionCheckBody

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionCheckBody from a JSON string
permission_check_body_instance = PermissionCheckBody.from_json(json)
# print the JSON string representation of the object
print(PermissionCheckBody.to_json())

# convert the object into a dict
permission_check_body_dict = permission_check_body_instance.to_dict()
# create an instance of PermissionCheckBody from a dict
permission_check_body_from_dict = PermissionCheckBody.from_dict(permission_check_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


