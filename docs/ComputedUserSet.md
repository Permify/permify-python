# ComputedUserSet

ComputedUserSet defines a set of computed users which includes the relation name.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relation** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.computed_user_set import ComputedUserSet

# TODO update the JSON string below
json = "{}"
# create an instance of ComputedUserSet from a JSON string
computed_user_set_instance = ComputedUserSet.from_json(json)
# print the JSON string representation of the object
print(ComputedUserSet.to_json())

# convert the object into a dict
computed_user_set_dict = computed_user_set_instance.to_dict()
# create an instance of ComputedUserSet from a dict
computed_user_set_form_dict = computed_user_set.from_dict(computed_user_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


