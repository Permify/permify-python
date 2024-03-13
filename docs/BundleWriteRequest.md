# BundleWriteRequest

BundleWriteRequest is used to request the writing of a bundle. It contains the tenant_id to identify the tenant and the Bundles object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bundles** | [**List[DataBundle]**](DataBundle.md) | Contains the bundle data to be written. | [optional] 

## Example

```python
from permify.models.bundle_write_request import BundleWriteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BundleWriteRequest from a JSON string
bundle_write_request_instance = BundleWriteRequest.from_json(json)
# print the JSON string representation of the object
print(BundleWriteRequest.to_json())

# convert the object into a dict
bundle_write_request_dict = bundle_write_request_instance.to_dict()
# create an instance of BundleWriteRequest from a dict
bundle_write_request_form_dict = bundle_write_request.from_dict(bundle_write_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


