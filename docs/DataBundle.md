# DataBundle

DataBundle is a message representing a bundle of data, which includes a name, a list of arguments, and a series of operations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | &#39;name&#39; is a simple string field representing the name of the DataBundle. | [optional] 
**arguments** | **List[str]** | &#39;arguments&#39; is a repeated field, which means it can contain multiple strings. These are used to store a list of arguments related to the DataBundle. | [optional] 
**operations** | [**List[V1Operation]**](V1Operation.md) | &#39;operations&#39; is a repeated field containing multiple Operation messages. Each Operation represents a specific action or set of actions to be performed. | [optional] 

## Example

```python
from openapi_client.models.data_bundle import DataBundle

# TODO update the JSON string below
json = "{}"
# create an instance of DataBundle from a JSON string
data_bundle_instance = DataBundle.from_json(json)
# print the JSON string representation of the object
print(DataBundle.to_json())

# convert the object into a dict
data_bundle_dict = data_bundle_instance.to_dict()
# create an instance of DataBundle from a dict
data_bundle_form_dict = data_bundle.from_dict(data_bundle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


