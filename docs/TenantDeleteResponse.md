# TenantDeleteResponse

TenantDeleteResponse is the message returned from the request to delete a tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant** | [**Tenant**](Tenant.md) |  | [optional] 

## Example

```python
from openapi_client.models.tenant_delete_response import TenantDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TenantDeleteResponse from a JSON string
tenant_delete_response_instance = TenantDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(TenantDeleteResponse.to_json())

# convert the object into a dict
tenant_delete_response_dict = tenant_delete_response_instance.to_dict()
# create an instance of TenantDeleteResponse from a dict
tenant_delete_response_form_dict = tenant_delete_response.from_dict(tenant_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


