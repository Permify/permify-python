# TenantListRequest

TenantListRequest is the message used for the request to list all tenants.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_size** | **int** | page_size is the number of tenants to be returned in the response. The value should be between 1 and 100. | [optional] 
**continuous_token** | **str** | continuous_token is an optional parameter used for pagination. It should be the value received in the previous response. | [optional] 

## Example

```python
from permify.models.tenant_list_request import TenantListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TenantListRequest from a JSON string
tenant_list_request_instance = TenantListRequest.from_json(json)
# print the JSON string representation of the object
print(TenantListRequest.to_json())

# convert the object into a dict
tenant_list_request_dict = tenant_list_request_instance.to_dict()
# create an instance of TenantListRequest from a dict
tenant_list_request_form_dict = tenant_list_request.from_dict(tenant_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


