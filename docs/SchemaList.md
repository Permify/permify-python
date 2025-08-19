# SchemaList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 

## Example

```python
from permify.models.schema_list import SchemaList

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaList from a JSON string
schema_list_instance = SchemaList.from_json(json)
# print the JSON string representation of the object
print SchemaList.to_json()

# convert the object into a dict
schema_list_dict = schema_list_instance.to_dict()
# create an instance of SchemaList from a dict
schema_list_form_dict = schema_list.from_dict(schema_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


