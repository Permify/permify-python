# DataWriteBody

DataWriteRequest defines the structure of a request for writing data. It contains the necessary information such as tenant_id, metadata, tuples and attributes for the write operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**DataWriteRequestMetadata**](DataWriteRequestMetadata.md) |  | [optional] 
**tuples** | [**List[Tuple]**](Tuple.md) | tuples contains the list of tuples (entity-relation-entity triples) that need to be written. | [optional] 
**attributes** | [**List[Attribute]**](Attribute.md) | attributes contains the list of attributes (entity-attribute-value triples) that need to be written. | [optional] 

## Example

```python
from permify.models.data_write_body import DataWriteBody

# TODO update the JSON string below
json = "{}"
# create an instance of DataWriteBody from a JSON string
data_write_body_instance = DataWriteBody.from_json(json)
# print the JSON string representation of the object
print(DataWriteBody.to_json())

# convert the object into a dict
data_write_body_dict = data_write_body_instance.to_dict()
# create an instance of DataWriteBody from a dict
data_write_body_from_dict = DataWriteBody.from_dict(data_write_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


