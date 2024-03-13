# PermissionLookupEntityResponse

PermissionLookupEntityResponse is the response message for the LookupEntity method in the Permission service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_ids** | **List[str]** | List of identifiers for entities that match the lookup. | [optional] 

## Example

```python
from openapi_client.models.permission_lookup_entity_response import PermissionLookupEntityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionLookupEntityResponse from a JSON string
permission_lookup_entity_response_instance = PermissionLookupEntityResponse.from_json(json)
# print the JSON string representation of the object
print(PermissionLookupEntityResponse.to_json())

# convert the object into a dict
permission_lookup_entity_response_dict = permission_lookup_entity_response_instance.to_dict()
# create an instance of PermissionLookupEntityResponse from a dict
permission_lookup_entity_response_form_dict = permission_lookup_entity_response.from_dict(permission_lookup_entity_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


