# V1Call

Call represents a call to a rule. It includes the name of the rule and the arguments passed to it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_name** | **str** |  | [optional] 
**arguments** | [**List[Argument]**](Argument.md) |  | [optional] 

## Example

```python
from permify.models.v1_call import V1Call

# TODO update the JSON string below
json = "{}"
# create an instance of V1Call from a JSON string
v1_call_instance = V1Call.from_json(json)
# print the JSON string representation of the object
print(V1Call.to_json())

# convert the object into a dict
v1_call_dict = v1_call_instance.to_dict()
# create an instance of V1Call from a dict
v1_call_from_dict = V1Call.from_dict(v1_call_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


