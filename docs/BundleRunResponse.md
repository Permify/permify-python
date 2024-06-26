# BundleRunResponse

BundleRunResponse is the response for a BundleRunRequest. It includes a snap_token, which may be used for tracking the execution or its results.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snap_token** | **str** | The snap token to avoid stale cache, see more details on [Snap Tokens](../../operations/snap-tokens) | [optional] 

## Example

```python
from permify.models.bundle_run_response import BundleRunResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BundleRunResponse from a JSON string
bundle_run_response_instance = BundleRunResponse.from_json(json)
# print the JSON string representation of the object
print(BundleRunResponse.to_json())

# convert the object into a dict
bundle_run_response_dict = bundle_run_response_instance.to_dict()
# create an instance of BundleRunResponse from a dict
bundle_run_response_from_dict = BundleRunResponse.from_dict(bundle_run_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


