# BundleWriteBody

BundleWriteRequest is used to request the writing of a bundle. It contains the tenant_id to identify the tenant and the Bundles object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bundles** | [**List[DataBundle]**](DataBundle.md) | Contains the bundle data to be written. | [optional] 

## Example

```python
from permify.models.bundle_write_body import BundleWriteBody

# TODO update the JSON string below
json = "{}"
# create an instance of BundleWriteBody from a JSON string
bundle_write_body_instance = BundleWriteBody.from_json(json)
# print the JSON string representation of the object
print BundleWriteBody.to_json()

# convert the object into a dict
bundle_write_body_dict = bundle_write_body_instance.to_dict()
# create an instance of BundleWriteBody from a dict
bundle_write_body_form_dict = bundle_write_body.from_dict(bundle_write_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


