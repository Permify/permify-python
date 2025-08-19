# BundleDeleteBody

BundleDeleteRequest is used to request the deletion of a bundle. It contains the tenant_id to specify the tenant and the name of the bundle to be deleted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the bundle to be deleted. | [optional] 

## Example

```python
from permify.models.bundle_delete_body import BundleDeleteBody

# TODO update the JSON string below
json = "{}"
# create an instance of BundleDeleteBody from a JSON string
bundle_delete_body_instance = BundleDeleteBody.from_json(json)
# print the JSON string representation of the object
print BundleDeleteBody.to_json()

# convert the object into a dict
bundle_delete_body_dict = bundle_delete_body_instance.to_dict()
# create an instance of BundleDeleteBody from a dict
bundle_delete_body_form_dict = bundle_delete_body.from_dict(bundle_delete_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


