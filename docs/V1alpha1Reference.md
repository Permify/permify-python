# V1alpha1Reference

Describes a resolved reference to a declaration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The fully qualified name of the declaration. | [optional] 
**overload_id** | **List[str]** | For references to functions, this is a list of &#x60;Overload.overload_id&#x60; values which match according to typing rules.  If the list has more than one element, overload resolution among the presented candidates must happen at runtime because of dynamic types. The type checker attempts to narrow down this list as much as possible.  Empty if this is not a reference to a [Decl.FunctionDecl][google.api.expr.v1alpha1.Decl.FunctionDecl]. | [optional] 
**value** | [**Constant**](Constant.md) |  | [optional] 

## Example

```python
from permify.models.v1alpha1_reference import V1alpha1Reference

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1Reference from a JSON string
v1alpha1_reference_instance = V1alpha1Reference.from_json(json)
# print the JSON string representation of the object
print V1alpha1Reference.to_json()

# convert the object into a dict
v1alpha1_reference_dict = v1alpha1_reference_instance.to_dict()
# create an instance of V1alpha1Reference from a dict
v1alpha1_reference_form_dict = v1alpha1_reference.from_dict(v1alpha1_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


