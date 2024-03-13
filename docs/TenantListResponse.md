# TenantListResponse

TenantListResponse is the message returned from the request to list all tenants.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenants** | [**List[Tenant]**](Tenant.md) | tenants is a list of tenants. | [optional] 
**continuous_token** | **str** | continuous_token is a string that can be used to paginate and retrieve the next set of results. | [optional] 

## Example

```python
from permify.models.tenant_list_response import TenantListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TenantListResponse from a JSON string
tenant_list_response_instance = TenantListResponse.from_json(json)
# print the JSON string representation of the object
print(TenantListResponse.to_json())

# convert the object into a dict
tenant_list_response_dict = tenant_list_response_instance.to_dict()
# create an instance of TenantListResponse from a dict
tenant_list_response_form_dict = tenant_list_response.from_dict(tenant_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


