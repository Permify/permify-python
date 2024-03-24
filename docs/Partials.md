# Partials


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**write** | **List[str]** |  | [optional] 
**delete** | **List[str]** |  | [optional] 
**update** | **List[str]** |  | [optional] 

## Example

```python
from permify.models.partials import Partials

# TODO update the JSON string below
json = "{}"
# create an instance of Partials from a JSON string
partials_instance = Partials.from_json(json)
# print the JSON string representation of the object
print(Partials.to_json())

# convert the object into a dict
partials_dict = partials_instance.to_dict()
# create an instance of Partials from a dict
partials_form_dict = partials.from_dict(partials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


