# PermissionBulkCheckRequestItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**Entity**](Entity.md) |  | [optional] 
**permission** | **str** | The action the user wants to perform on the resource | [optional] 
**subject** | [**Subject**](Subject.md) |  | [optional] 

## Example

```python
from permify.models.permission_bulk_check_request_item import PermissionBulkCheckRequestItem

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionBulkCheckRequestItem from a JSON string
permission_bulk_check_request_item_instance = PermissionBulkCheckRequestItem.from_json(json)
# print the JSON string representation of the object
print PermissionBulkCheckRequestItem.to_json()

# convert the object into a dict
permission_bulk_check_request_item_dict = permission_bulk_check_request_item_instance.to_dict()
# create an instance of PermissionBulkCheckRequestItem from a dict
permission_bulk_check_request_item_form_dict = permission_bulk_check_request_item.from_dict(permission_bulk_check_request_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


