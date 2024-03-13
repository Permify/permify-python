# BundleRunResponse

BundleRunResponse is the response for a BundleRunRequest. It includes a snap_token, which may be used for tracking the execution or its results.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snap_token** | **str** | Token related to the bundle execution. | [optional] 

## Example

```python
from openapi_client.models.bundle_run_response import BundleRunResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BundleRunResponse from a JSON string
bundle_run_response_instance = BundleRunResponse.from_json(json)
# print the JSON string representation of the object
print(BundleRunResponse.to_json())

# convert the object into a dict
bundle_run_response_dict = bundle_run_response_instance.to_dict()
# create an instance of BundleRunResponse from a dict
bundle_run_response_form_dict = bundle_run_response.from_dict(bundle_run_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


