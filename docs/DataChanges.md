# DataChanges

DataChanges represent changes in data with a snap token and a list of data change objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snap_token** | **str** | The snapshot token. | [optional] 
**data_changes** | [**List[DataChange]**](DataChange.md) | The list of data changes. | [optional] 

## Example

```python
from permify.models.data_changes import DataChanges

# TODO update the JSON string below
json = "{}"
# create an instance of DataChanges from a JSON string
data_changes_instance = DataChanges.from_json(json)
# print the JSON string representation of the object
print(DataChanges.to_json())

# convert the object into a dict
data_changes_dict = data_changes_instance.to_dict()
# create an instance of DataChanges from a dict
data_changes_form_dict = data_changes.from_dict(data_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


