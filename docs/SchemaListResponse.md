# SchemaListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**head** | **str** |  | [optional] 
**schemas** | [**List[SchemaList]**](SchemaList.md) |  | [optional] 
**continuous_token** | **str** | continuous_token is a string that can be used to paginate and retrieve the next set of results. | [optional] 

## Example

```python
from permify.models.schema_list_response import SchemaListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaListResponse from a JSON string
schema_list_response_instance = SchemaListResponse.from_json(json)
# print the JSON string representation of the object
print(SchemaListResponse.to_json())

# convert the object into a dict
schema_list_response_dict = schema_list_response_instance.to_dict()
# create an instance of SchemaListResponse from a dict
schema_list_response_form_dict = schema_list_response.from_dict(schema_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


