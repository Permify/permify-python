# AttributeReadRequestMetadata

AttributeReadRequestMetadata defines the structure for the metadata of an attribute read request. It includes the snap_token associated with a particular state of the database.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snap_token** | **str** | The snap token to avoid stale cache, see more details on [Snap Tokens](../../operations/snap-tokens) | [optional] 

## Example

```python
from permify.models.attribute_read_request_metadata import AttributeReadRequestMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeReadRequestMetadata from a JSON string
attribute_read_request_metadata_instance = AttributeReadRequestMetadata.from_json(json)
# print the JSON string representation of the object
print(AttributeReadRequestMetadata.to_json())

# convert the object into a dict
attribute_read_request_metadata_dict = attribute_read_request_metadata_instance.to_dict()
# create an instance of AttributeReadRequestMetadata from a dict
attribute_read_request_metadata_from_dict = AttributeReadRequestMetadata.from_dict(attribute_read_request_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


