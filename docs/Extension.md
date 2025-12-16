# Extension

An extension that was requested for the source expression.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**affected_components** | [**List[Component]**](Component.md) | If set, the listed components must understand the extension for the expression to evaluate correctly.  This field has set semantics, repeated values should be deduplicated. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 

## Example

```python
from permify.models.extension import Extension

# TODO update the JSON string below
json = "{}"
# create an instance of Extension from a JSON string
extension_instance = Extension.from_json(json)
# print the JSON string representation of the object
print Extension.to_json()

# convert the object into a dict
extension_dict = extension_instance.to_dict()
# create an instance of Extension from a dict
extension_form_dict = extension.from_dict(extension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


