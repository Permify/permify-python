# SchemaListBody

SchemaListRequest is the request message for the List method in the Schema service. It contains tenant_id for which the schemas are to be listed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_size** | **int** | page_size is the number of schemas to be returned in the response. The value should be between 1 and 100. | [optional] 
**continuous_token** | **str** | continuous_token is an optional parameter used for pagination. It should be the value received in the previous response. | [optional] 

## Example

```python
from permify.models.schema_list_body import SchemaListBody

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaListBody from a JSON string
schema_list_body_instance = SchemaListBody.from_json(json)
# print the JSON string representation of the object
print(SchemaListBody.to_json())

# convert the object into a dict
schema_list_body_dict = schema_list_body_instance.to_dict()
# create an instance of SchemaListBody from a dict
schema_list_body_from_dict = SchemaListBody.from_dict(schema_list_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


