# PermissionsCheckRequest

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
from permify.models.permissions_check_request import PermissionsCheckRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionsCheckRequest from a JSON string
permissions_check_request_instance = PermissionsCheckRequest.from_json(json)
# print the JSON string representation of the object
print(PermissionsCheckRequest.to_json())

# convert the object into a dict
permissions_check_request_dict = permissions_check_request_instance.to_dict()
# create an instance of PermissionsCheckRequest from a dict
permissions_check_request_form_dict = permissions_check_request.from_dict(permissions_check_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


