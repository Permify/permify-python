# DataAttributesReadRequest

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
from permify.models.data_attributes_read_request import DataAttributesReadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DataAttributesReadRequest from a JSON string
data_attributes_read_request_instance = DataAttributesReadRequest.from_json(json)
# print the JSON string representation of the object
print(DataAttributesReadRequest.to_json())

# convert the object into a dict
data_attributes_read_request_dict = data_attributes_read_request_instance.to_dict()
# create an instance of DataAttributesReadRequest from a dict
data_attributes_read_request_from_dict = DataAttributesReadRequest.from_dict(data_attributes_read_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


