# DataDeleteResponse

DataDeleteResponse defines the structure of the response to a data delete request. It includes a snap_token representing the state of the database after the deletion.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snap_token** | **str** | The snap token to avoid stale cache, see more details on [Snap Tokens](../../operations/snap-tokens) | [optional] 

## Example

```python
from permify.models.data_delete_response import DataDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DataDeleteResponse from a JSON string
data_delete_response_instance = DataDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(DataDeleteResponse.to_json())

# convert the object into a dict
data_delete_response_dict = data_delete_response_instance.to_dict()
# create an instance of DataDeleteResponse from a dict
data_delete_response_form_dict = data_delete_response.from_dict(data_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


