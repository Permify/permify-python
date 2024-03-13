# StreamResultOfWatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**WatchResponse**](WatchResponse.md) |  | [optional] 
**error** | [**Status**](Status.md) |  | [optional] 

## Example

```python
from openapi_client.models.stream_result_of_watch_response import StreamResultOfWatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StreamResultOfWatchResponse from a JSON string
stream_result_of_watch_response_instance = StreamResultOfWatchResponse.from_json(json)
# print the JSON string representation of the object
print(StreamResultOfWatchResponse.to_json())

# convert the object into a dict
stream_result_of_watch_response_dict = stream_result_of_watch_response_instance.to_dict()
# create an instance of StreamResultOfWatchResponse from a dict
stream_result_of_watch_response_form_dict = stream_result_of_watch_response.from_dict(stream_result_of_watch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


