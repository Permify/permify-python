# Tenant

Tenant represents a tenant with an id, a name, and a timestamp indicating when it was created.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the tenant. | [optional] 
**name** | **str** | The name of the tenant. | [optional] 
**created_at** | **datetime** | The time at which the tenant was created. | [optional] 

## Example

```python
from openapi_client.models.tenant import Tenant

# TODO update the JSON string below
json = "{}"
# create an instance of Tenant from a JSON string
tenant_instance = Tenant.from_json(json)
# print the JSON string representation of the object
print(Tenant.to_json())

# convert the object into a dict
tenant_dict = tenant_instance.to_dict()
# create an instance of Tenant from a dict
tenant_form_dict = tenant.from_dict(tenant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


