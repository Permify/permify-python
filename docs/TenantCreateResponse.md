# TenantCreateResponse

TenantCreateResponse is the message returned from the request to create a tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant** | [**Tenant**](Tenant.md) |  | [optional] 

## Example

```python
from permify.models.tenant_create_response import TenantCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TenantCreateResponse from a JSON string
tenant_create_response_instance = TenantCreateResponse.from_json(json)
# print the JSON string representation of the object
print TenantCreateResponse.to_json()

# convert the object into a dict
tenant_create_response_dict = tenant_create_response_instance.to_dict()
# create an instance of TenantCreateResponse from a dict
tenant_create_response_form_dict = tenant_create_response.from_dict(tenant_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


