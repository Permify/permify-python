# ReadAttributesBody

AttributeReadRequest defines the structure of a request for reading attributes. It includes the tenant_id, metadata, attribute filter, page size for pagination, and a continuous token for multi-page results.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**AttributeReadRequestMetadata**](AttributeReadRequestMetadata.md) |  | [optional] 
**filter** | [**AttributeFilter**](AttributeFilter.md) |  | [optional] 
**page_size** | **int** | page_size specifies the number of results to return in a single page. If more results are available, a continuous_token is included in the response. | [optional] 
**continuous_token** | **str** | continuous_token is used in case of paginated reads to get the next page of results. | [optional] 

## Example

```python
from permify.models.read_attributes_body import ReadAttributesBody

# TODO update the JSON string below
json = "{}"
# create an instance of ReadAttributesBody from a JSON string
read_attributes_body_instance = ReadAttributesBody.from_json(json)
# print the JSON string representation of the object
print(ReadAttributesBody.to_json())

# convert the object into a dict
read_attributes_body_dict = read_attributes_body_instance.to_dict()
# create an instance of ReadAttributesBody from a dict
read_attributes_body_from_dict = ReadAttributesBody.from_dict(read_attributes_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


