# RunBundleBody

BundleRunRequest is used to request the execution of a bundle. It includes tenant_id, the name of the bundle, and additional arguments for execution.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the bundle to be executed. | [optional] 
**arguments** | **Dict[str, str]** | Additional key-value pairs for execution arguments. | [optional] 

## Example

```python
from permify.models.run_bundle_body import RunBundleBody

# TODO update the JSON string below
json = "{}"
# create an instance of RunBundleBody from a JSON string
run_bundle_body_instance = RunBundleBody.from_json(json)
# print the JSON string representation of the object
print(RunBundleBody.to_json())

# convert the object into a dict
run_bundle_body_dict = run_bundle_body_instance.to_dict()
# create an instance of RunBundleBody from a dict
run_bundle_body_from_dict = RunBundleBody.from_dict(run_bundle_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


