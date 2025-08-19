# AttributeReadResponse

AttributeReadResponse defines the structure of the response to an attribute read request. It includes the attributes retrieved and a continuous token for handling result pagination.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**List[Attribute]**](Attribute.md) | attributes is a list of the attributes retrieved in the read operation. | [optional] 
**continuous_token** | **str** | continuous_token is used in the case of paginated reads to retrieve the next page of results. | [optional] 

## Example

```python
from permify.models.attribute_read_response import AttributeReadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeReadResponse from a JSON string
attribute_read_response_instance = AttributeReadResponse.from_json(json)
# print the JSON string representation of the object
print AttributeReadResponse.to_json()

# convert the object into a dict
attribute_read_response_dict = attribute_read_response_instance.to_dict()
# create an instance of AttributeReadResponse from a dict
attribute_read_response_form_dict = attribute_read_response.from_dict(attribute_read_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


