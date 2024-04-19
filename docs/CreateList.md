# CreateList

A list creation expression.  Lists may either be homogenous, e.g. `[1, 2, 3]`, or heterogeneous, e.g. `dyn([1, 'hello', 2.0])`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elements** | [**List[Expr]**](Expr.md) | The elements part of the list. | [optional] 
**optional_indices** | **List[int]** | The indices within the elements list which are marked as optional elements.  When an optional-typed value is present, the value it contains is included in the list. If the optional-typed value is absent, the list element is omitted from the CreateList result. | [optional] 

## Example

```python
from permify.models.create_list import CreateList

# TODO update the JSON string below
json = "{}"
# create an instance of CreateList from a JSON string
create_list_instance = CreateList.from_json(json)
# print the JSON string representation of the object
print(CreateList.to_json())

# convert the object into a dict
create_list_dict = create_list_instance.to_dict()
# create an instance of CreateList from a dict
create_list_from_dict = CreateList.from_dict(create_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


