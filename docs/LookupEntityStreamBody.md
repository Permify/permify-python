# LookupEntityStreamBody

PermissionLookupEntityRequest is the request message for the LookupEntity method in the Permission service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**PermissionLookupEntityRequestMetadata**](PermissionLookupEntityRequestMetadata.md) |  | [optional] 
**entity_type** | **str** | Type of the entity to lookup, required, must start with a letter and can include alphanumeric and underscore, max 64 bytes. | [optional] 
**permission** | **str** | Name of the permission to check, required, must start with a letter and can include alphanumeric and underscore, max 64 bytes. | [optional] 
**subject** | [**Subject**](Subject.md) |  | [optional] 
**context** | [**Context**](Context.md) |  | [optional] 
**page_size** | **int** | page_size is the number of tenants to be returned in the response. The value should be between 1 and 100. | [optional] 
**continuous_token** | **str** | continuous_token is an optional parameter used for pagination. It should be the value received in the previous response. | [optional] 

## Example

```python
from permify.models.lookup_entity_stream_body import LookupEntityStreamBody

# TODO update the JSON string below
json = "{}"
# create an instance of LookupEntityStreamBody from a JSON string
lookup_entity_stream_body_instance = LookupEntityStreamBody.from_json(json)
# print the JSON string representation of the object
print(LookupEntityStreamBody.to_json())

# convert the object into a dict
lookup_entity_stream_body_dict = lookup_entity_stream_body_instance.to_dict()
# create an instance of LookupEntityStreamBody from a dict
lookup_entity_stream_body_from_dict = LookupEntityStreamBody.from_dict(lookup_entity_stream_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


