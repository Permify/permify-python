# WatchBody

WatchRequest is the request message for the Watch RPC. It contains the details needed to establish a watch stream.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snap_token** | **str** | The snap token to avoid stale cache, see more details on [Snap Tokens](../../operations/snap-tokens). | [optional] 

## Example

```python
from permify.models.watch_body import WatchBody

# TODO update the JSON string below
json = "{}"
# create an instance of WatchBody from a JSON string
watch_body_instance = WatchBody.from_json(json)
# print the JSON string representation of the object
print(WatchBody.to_json())

# convert the object into a dict
watch_body_dict = watch_body_instance.to_dict()
# create an instance of WatchBody from a dict
watch_body_from_dict = WatchBody.from_dict(watch_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


