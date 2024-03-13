# WatchResponse

WatchResponse is the response message for the Watch RPC. It contains the changes in the data that are being watched.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**DataChanges**](DataChanges.md) |  | [optional] 

## Example

```python
from permify.models.watch_response import WatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WatchResponse from a JSON string
watch_response_instance = WatchResponse.from_json(json)
# print the JSON string representation of the object
print(WatchResponse.to_json())

# convert the object into a dict
watch_response_dict = watch_response_instance.to_dict()
# create an instance of WatchResponse from a dict
watch_response_form_dict = watch_response.from_dict(watch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


