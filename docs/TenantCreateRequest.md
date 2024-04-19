# TenantCreateRequest

TenantCreateRequest is the message used for the request to create a tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id is a unique identifier for the tenant. | [optional] 
**name** | **str** | name is the name of the tenant. | [optional] 

## Example

```python
from permify.models.tenant_create_request import TenantCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TenantCreateRequest from a JSON string
tenant_create_request_instance = TenantCreateRequest.from_json(json)
# print the JSON string representation of the object
print(TenantCreateRequest.to_json())

# convert the object into a dict
tenant_create_request_dict = tenant_create_request_instance.to_dict()
# create an instance of TenantCreateRequest from a dict
tenant_create_request_from_dict = TenantCreateRequest.from_dict(tenant_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


