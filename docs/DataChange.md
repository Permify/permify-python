# DataChange

DataChange represents a single change in data, with an operation type and the actual change which could be a tuple or an attribute.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | [**DataChangeOperation**](DataChangeOperation.md) |  | [optional] 
**tuple** | [**Tuple**](Tuple.md) |  | [optional] 
**attribute** | [**Attribute**](Attribute.md) |  | [optional] 

## Example

```python
from permify.models.data_change import DataChange

# TODO update the JSON string below
json = "{}"
# create an instance of DataChange from a JSON string
data_change_instance = DataChange.from_json(json)
# print the JSON string representation of the object
print DataChange.to_json()

# convert the object into a dict
data_change_dict = data_change_instance.to_dict()
# create an instance of DataChange from a dict
data_change_form_dict = data_change.from_dict(data_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


