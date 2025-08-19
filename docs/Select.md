# Select

A field selection expression. e.g. `request.auth`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operand** | [**Expr**](Expr.md) |  | [optional] 
**field** | **str** | Required. The name of the field to select.  For example, in the select expression &#x60;request.auth&#x60;, the &#x60;auth&#x60; portion of the expression would be the &#x60;field&#x60;. | [optional] 
**test_only** | **bool** | Whether the select is to be interpreted as a field presence test.  This results from the macro &#x60;has(request.auth)&#x60;. | [optional] 

## Example

```python
from permify.models.select import Select

# TODO update the JSON string below
json = "{}"
# create an instance of Select from a JSON string
select_instance = Select.from_json(json)
# print the JSON string representation of the object
print Select.to_json()

# convert the object into a dict
select_dict = select_instance.to_dict()
# create an instance of Select from a dict
select_form_dict = select.from_dict(select_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


