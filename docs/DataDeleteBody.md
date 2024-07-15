# DataDeleteBody

DataDeleteRequest defines the structure of a request to delete data. It includes the tenant_id and filters for selecting tuples and attributes to be deleted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tuple_filter** | [**TupleFilter**](TupleFilter.md) |  | [optional] 
**attribute_filter** | [**AttributeFilter**](AttributeFilter.md) |  | [optional] 

## Example

```python
from permify.models.data_delete_body import DataDeleteBody

# TODO update the JSON string below
json = "{}"
# create an instance of DataDeleteBody from a JSON string
data_delete_body_instance = DataDeleteBody.from_json(json)
# print the JSON string representation of the object
print(DataDeleteBody.to_json())

# convert the object into a dict
data_delete_body_dict = data_delete_body_instance.to_dict()
# create an instance of DataDeleteBody from a dict
data_delete_body_from_dict = DataDeleteBody.from_dict(data_delete_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


