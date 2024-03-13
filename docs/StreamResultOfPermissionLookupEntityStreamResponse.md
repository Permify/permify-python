# StreamResultOfPermissionLookupEntityStreamResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**PermissionLookupEntityStreamResponse**](PermissionLookupEntityStreamResponse.md) |  | [optional] 
**error** | [**Status**](Status.md) |  | [optional] 

## Example

```python
from permify.models.stream_result_of_permission_lookup_entity_stream_response import StreamResultOfPermissionLookupEntityStreamResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StreamResultOfPermissionLookupEntityStreamResponse from a JSON string
stream_result_of_permission_lookup_entity_stream_response_instance = StreamResultOfPermissionLookupEntityStreamResponse.from_json(json)
# print the JSON string representation of the object
print(StreamResultOfPermissionLookupEntityStreamResponse.to_json())

# convert the object into a dict
stream_result_of_permission_lookup_entity_stream_response_dict = stream_result_of_permission_lookup_entity_stream_response_instance.to_dict()
# create an instance of StreamResultOfPermissionLookupEntityStreamResponse from a dict
stream_result_of_permission_lookup_entity_stream_response_form_dict = stream_result_of_permission_lookup_entity_stream_response.from_dict(stream_result_of_permission_lookup_entity_stream_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


