# Ident

An identifier expression. e.g. `request`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Required. Holds a single, unqualified identifier, possibly preceded by a &#39;.&#39;.  Qualified names are represented by the [Expr.Select][google.api.expr.v1alpha1.Expr.Select] expression. | [optional] 

## Example

```python
from permify.models.ident import Ident

# TODO update the JSON string below
json = "{}"
# create an instance of Ident from a JSON string
ident_instance = Ident.from_json(json)
# print the JSON string representation of the object
print(Ident.to_json())

# convert the object into a dict
ident_dict = ident_instance.to_dict()
# create an instance of Ident from a dict
ident_from_dict = Ident.from_dict(ident_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


