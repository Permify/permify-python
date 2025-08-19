# PermissionLookupEntityStreamResponse

PermissionLookupEntityStreamResponse is the response message for the LookupEntityStream method in the Permission service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **str** | Identifier for an entity that matches the lookup. | [optional] 
**continuous_token** | **str** | continuous_token is a string that can be used to paginate and retrieve the next set of results. | [optional] 

## Example

```python
from permify.models.permission_lookup_entity_stream_response import PermissionLookupEntityStreamResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionLookupEntityStreamResponse from a JSON string
permission_lookup_entity_stream_response_instance = PermissionLookupEntityStreamResponse.from_json(json)
# print the JSON string representation of the object
print PermissionLookupEntityStreamResponse.to_json()

# convert the object into a dict
permission_lookup_entity_stream_response_dict = permission_lookup_entity_stream_response_instance.to_dict()
# create an instance of PermissionLookupEntityStreamResponse from a dict
permission_lookup_entity_stream_response_form_dict = permission_lookup_entity_stream_response.from_dict(permission_lookup_entity_stream_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


