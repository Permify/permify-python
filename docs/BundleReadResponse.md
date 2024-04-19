# BundleReadResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bundle** | [**DataBundle**](DataBundle.md) |  | [optional] 

## Example

```python
from permify.models.bundle_read_response import BundleReadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BundleReadResponse from a JSON string
bundle_read_response_instance = BundleReadResponse.from_json(json)
# print the JSON string representation of the object
print(BundleReadResponse.to_json())

# convert the object into a dict
bundle_read_response_dict = bundle_read_response_instance.to_dict()
# create an instance of BundleReadResponse from a dict
bundle_read_response_from_dict = BundleReadResponse.from_dict(bundle_read_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


