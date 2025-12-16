# PermissionBulkCheckResponse

PermissionBulkCheckResponse is the response message for the BulkCheck method in the Permission service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[PermissionCheckResponse]**](PermissionCheckResponse.md) | List of permission check responses corresponding to each request. | [optional] 

## Example

```python
from permify.models.permission_bulk_check_response import PermissionBulkCheckResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionBulkCheckResponse from a JSON string
permission_bulk_check_response_instance = PermissionBulkCheckResponse.from_json(json)
# print the JSON string representation of the object
print PermissionBulkCheckResponse.to_json()

# convert the object into a dict
permission_bulk_check_response_dict = permission_bulk_check_response_instance.to_dict()
# create an instance of PermissionBulkCheckResponse from a dict
permission_bulk_check_response_form_dict = permission_bulk_check_response.from_dict(permission_bulk_check_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


