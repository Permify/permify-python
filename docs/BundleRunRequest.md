# BundleRunRequest

BundleRunRequest is used to request the execution of a bundle. It includes tenant_id, the name of the bundle, and additional arguments for execution.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the bundle to be executed. | [optional] 
**arguments** | **Dict[str, str]** | Additional key-value pairs for execution arguments. | [optional] 

## Example

```python
from permify.models.bundle_run_request import BundleRunRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BundleRunRequest from a JSON string
bundle_run_request_instance = BundleRunRequest.from_json(json)
# print the JSON string representation of the object
print(BundleRunRequest.to_json())

# convert the object into a dict
bundle_run_request_dict = bundle_run_request_instance.to_dict()
# create an instance of BundleRunRequest from a dict
bundle_run_request_from_dict = BundleRunRequest.from_dict(bundle_run_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


