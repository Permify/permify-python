# DataRelationshipsReadRequest

RelationshipReadRequest defines the structure of a request for reading relationships. It contains the necessary information such as tenant_id, metadata, and filter for the read operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**RelationshipReadRequestMetadata**](RelationshipReadRequestMetadata.md) |  | [optional] 
**filter** | [**TupleFilter**](TupleFilter.md) |  | [optional] 
**page_size** | **int** | page_size specifies the number of results to return in a single page. If more results are available, a continuous_token is included in the response. | [optional] 
**continuous_token** | **str** | continuous_token is used in case of paginated reads to get the next page of results. | [optional] 

## Example

```python
from permify.models.data_relationships_read_request import DataRelationshipsReadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DataRelationshipsReadRequest from a JSON string
data_relationships_read_request_instance = DataRelationshipsReadRequest.from_json(json)
# print the JSON string representation of the object
print(DataRelationshipsReadRequest.to_json())

# convert the object into a dict
data_relationships_read_request_dict = data_relationships_read_request_instance.to_dict()
# create an instance of DataRelationshipsReadRequest from a dict
data_relationships_read_request_from_dict = DataRelationshipsReadRequest.from_dict(data_relationships_read_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


