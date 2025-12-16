# BulkCheckBody

PermissionBulkCheckRequest is the request message for the BulkCheck method in the Permission service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**PermissionCheckRequestMetadata**](PermissionCheckRequestMetadata.md) |  | [optional] 
**items** | [**List[PermissionBulkCheckRequestItem]**](PermissionBulkCheckRequestItem.md) | List of permission check requests, maximum 100 items. | [optional] 
**context** | [**Context**](Context.md) |  | [optional] 
**arguments** | [**List[Argument]**](Argument.md) | Additional arguments associated with this request. | [optional] 

## Example

```python
from permify.models.bulk_check_body import BulkCheckBody

# TODO update the JSON string below
json = "{}"
# create an instance of BulkCheckBody from a JSON string
bulk_check_body_instance = BulkCheckBody.from_json(json)
# print the JSON string representation of the object
print BulkCheckBody.to_json()

# convert the object into a dict
bulk_check_body_dict = bulk_check_body_instance.to_dict()
# create an instance of BulkCheckBody from a dict
bulk_check_body_form_dict = bulk_check_body.from_dict(bulk_check_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


