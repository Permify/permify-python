# AbstractType

Application defined abstract type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The fully qualified name of this abstract type. | [optional] 
**parameter_types** | [**List[V1alpha1Type]**](V1alpha1Type.md) | Parameter types for this abstract type. | [optional] 

## Example

```python
from openapi_client.models.abstract_type import AbstractType

# TODO update the JSON string below
json = "{}"
# create an instance of AbstractType from a JSON string
abstract_type_instance = AbstractType.from_json(json)
# print the JSON string representation of the object
print(AbstractType.to_json())

# convert the object into a dict
abstract_type_dict = abstract_type_instance.to_dict()
# create an instance of AbstractType from a dict
abstract_type_form_dict = abstract_type.from_dict(abstract_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


