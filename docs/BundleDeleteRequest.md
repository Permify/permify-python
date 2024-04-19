# BundleDeleteRequest

BundleDeleteRequest is used to request the deletion of a bundle. It contains the tenant_id to specify the tenant and the name of the bundle to be deleted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the bundle to be deleted. | [optional] 

## Example

```python
from permify.models.bundle_delete_request import BundleDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BundleDeleteRequest from a JSON string
bundle_delete_request_instance = BundleDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(BundleDeleteRequest.to_json())

# convert the object into a dict
bundle_delete_request_dict = bundle_delete_request_instance.to_dict()
# create an instance of BundleDeleteRequest from a dict
bundle_delete_request_from_dict = BundleDeleteRequest.from_dict(bundle_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


