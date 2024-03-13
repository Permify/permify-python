# SchemasListRequest

SchemaListRequest is the request message for the List method in the Schema service. It contains tenant_id for which the schemas are to be listed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_size** | **int** | page_size is the number of tenants to be returned in the response. The value should be between 1 and 100. | [optional] 
**continuous_token** | **str** | continuous_token is an optional parameter used for pagination. It should be the value received in the previous response. | [optional] 

## Example

```python
from openapi_client.models.schemas_list_request import SchemasListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SchemasListRequest from a JSON string
schemas_list_request_instance = SchemasListRequest.from_json(json)
# print the JSON string representation of the object
print(SchemasListRequest.to_json())

# convert the object into a dict
schemas_list_request_dict = schemas_list_request_instance.to_dict()
# create an instance of SchemasListRequest from a dict
schemas_list_request_form_dict = schemas_list_request.from_dict(schemas_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


