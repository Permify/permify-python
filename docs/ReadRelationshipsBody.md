# ReadRelationshipsBody

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
from permify.models.read_relationships_body import ReadRelationshipsBody

# TODO update the JSON string below
json = "{}"
# create an instance of ReadRelationshipsBody from a JSON string
read_relationships_body_instance = ReadRelationshipsBody.from_json(json)
# print the JSON string representation of the object
print(ReadRelationshipsBody.to_json())

# convert the object into a dict
read_relationships_body_dict = read_relationships_body_instance.to_dict()
# create an instance of ReadRelationshipsBody from a dict
read_relationships_body_from_dict = ReadRelationshipsBody.from_dict(read_relationships_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


