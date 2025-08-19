# DataWriteResponse

DataWriteResponse defines the structure of the response after writing data. It contains the snap_token generated after the write operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snap_token** | **str** | The snap token to avoid stale cache, see more details on [Snap Tokens](../../operations/snap-tokens). | [optional] 

## Example

```python
from permify.models.data_write_response import DataWriteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DataWriteResponse from a JSON string
data_write_response_instance = DataWriteResponse.from_json(json)
# print the JSON string representation of the object
print DataWriteResponse.to_json()

# convert the object into a dict
data_write_response_dict = data_write_response_instance.to_dict()
# create an instance of DataWriteResponse from a dict
data_write_response_form_dict = data_write_response.from_dict(data_write_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


