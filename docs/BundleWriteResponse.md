# BundleWriteResponse

BundleWriteResponse is the response for a BundleWriteRequest. It includes a name which could be used as an identifier or acknowledgment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**names** | **List[str]** | Identifier or acknowledgment of the written bundle. | [optional] 

## Example

```python
from openapi_client.models.bundle_write_response import BundleWriteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BundleWriteResponse from a JSON string
bundle_write_response_instance = BundleWriteResponse.from_json(json)
# print the JSON string representation of the object
print(BundleWriteResponse.to_json())

# convert the object into a dict
bundle_write_response_dict = bundle_write_response_instance.to_dict()
# create an instance of BundleWriteResponse from a dict
bundle_write_response_form_dict = bundle_write_response.from_dict(bundle_write_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


