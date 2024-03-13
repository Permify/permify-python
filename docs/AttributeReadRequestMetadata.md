# AttributeReadRequestMetadata

AttributeReadRequestMetadata defines the structure for the metadata of an attribute read request. It includes the snap_token associated with a particular state of the database.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snap_token** | **str** | snap_token represents a specific state or \&quot;snapshot\&quot; of the database. | [optional] 

## Example

```python
from openapi_client.models.attribute_read_request_metadata import AttributeReadRequestMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeReadRequestMetadata from a JSON string
attribute_read_request_metadata_instance = AttributeReadRequestMetadata.from_json(json)
# print the JSON string representation of the object
print(AttributeReadRequestMetadata.to_json())

# convert the object into a dict
attribute_read_request_metadata_dict = attribute_read_request_metadata_instance.to_dict()
# create an instance of AttributeReadRequestMetadata from a dict
attribute_read_request_metadata_form_dict = attribute_read_request_metadata.from_dict(attribute_read_request_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


