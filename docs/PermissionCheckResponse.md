# PermissionCheckResponse

PermissionCheckResponse is the response message for the Check method in the Permission service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can** | [**CheckResult**](CheckResult.md) |  | [optional] 
**metadata** | [**PermissionCheckResponseMetadata**](PermissionCheckResponseMetadata.md) |  | [optional] 

## Example

```python
from permify.models.permission_check_response import PermissionCheckResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionCheckResponse from a JSON string
permission_check_response_instance = PermissionCheckResponse.from_json(json)
# print the JSON string representation of the object
print(PermissionCheckResponse.to_json())

# convert the object into a dict
permission_check_response_dict = permission_check_response_instance.to_dict()
# create an instance of PermissionCheckResponse from a dict
permission_check_response_form_dict = permission_check_response.from_dict(permission_check_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


