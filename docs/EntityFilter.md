# EntityFilter

EntityFilter is used to filter entities based on the type and ids.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**ids** | **List[str]** |  | [optional] 

## Example

```python
from permify.models.entity_filter import EntityFilter

# TODO update the JSON string below
json = "{}"
# create an instance of EntityFilter from a JSON string
entity_filter_instance = EntityFilter.from_json(json)
# print the JSON string representation of the object
print EntityFilter.to_json()

# convert the object into a dict
entity_filter_dict = entity_filter_instance.to_dict()
# create an instance of EntityFilter from a dict
entity_filter_form_dict = entity_filter.from_dict(entity_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


