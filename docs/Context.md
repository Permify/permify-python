# Context

Context encapsulates the information related to a single operation, including the tuples involved and the associated attributes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tuples** | [**List[Tuple]**](Tuple.md) | A repeated field of tuples involved in the operation. | [optional] 
**attributes** | [**List[Attribute]**](Attribute.md) | A repeated field of attributes associated with the operation. | [optional] 
**data** | **object** | Additional data associated with the context. | [optional] 

## Example

```python
from permify.models.context import Context

# TODO update the JSON string below
json = "{}"
# create an instance of Context from a JSON string
context_instance = Context.from_json(json)
# print the JSON string representation of the object
print(Context.to_json())

# convert the object into a dict
context_dict = context_instance.to_dict()
# create an instance of Context from a dict
context_from_dict = Context.from_dict(context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


