# PermissionsLookupEntityRequest

PermissionLookupEntityRequest is the request message for the LookupEntity method in the Permission service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**PermissionLookupEntityRequestMetadata**](PermissionLookupEntityRequestMetadata.md) |  | [optional] 
**entity_type** | **str** | Type of the entity to lookup, required, must start with a letter and can include alphanumeric and underscore, max 64 bytes. | [optional] 
**permission** | **str** | Name of the permission to check, required, must start with a letter and can include alphanumeric and underscore, max 64 bytes. | [optional] 
**subject** | [**Subject**](Subject.md) |  | [optional] 
**context** | [**Context**](Context.md) |  | [optional] 

## Example

```python
from permify.models.permissions_lookup_entity_request import PermissionsLookupEntityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionsLookupEntityRequest from a JSON string
permissions_lookup_entity_request_instance = PermissionsLookupEntityRequest.from_json(json)
# print the JSON string representation of the object
print(PermissionsLookupEntityRequest.to_json())

# convert the object into a dict
permissions_lookup_entity_request_dict = permissions_lookup_entity_request_instance.to_dict()
# create an instance of PermissionsLookupEntityRequest from a dict
permissions_lookup_entity_request_from_dict = PermissionsLookupEntityRequest.from_dict(permissions_lookup_entity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


