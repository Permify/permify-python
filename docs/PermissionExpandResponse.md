# PermissionExpandResponse

PermissionExpandResponse is the response message for the Expand method in the Permission service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tree** | [**Expand**](Expand.md) |  | [optional] 

## Example

```python
from openapi_client.models.permission_expand_response import PermissionExpandResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionExpandResponse from a JSON string
permission_expand_response_instance = PermissionExpandResponse.from_json(json)
# print the JSON string representation of the object
print(PermissionExpandResponse.to_json())

# convert the object into a dict
permission_expand_response_dict = permission_expand_response_instance.to_dict()
# create an instance of PermissionExpandResponse from a dict
permission_expand_response_form_dict = permission_expand_response.from_dict(permission_expand_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


