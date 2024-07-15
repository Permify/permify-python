# Rewrite

The Rewrite message represents a specific rewrite operation. This operation could be one of the following: union, intersection, or exclusion.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rewrite_operation** | [**RewriteOperation**](RewriteOperation.md) |  | [optional] 
**children** | [**List[Child]**](Child.md) | A list of children that are operated upon by the rewrite operation. | [optional] 

## Example

```python
from permify.models.rewrite import Rewrite

# TODO update the JSON string below
json = "{}"
# create an instance of Rewrite from a JSON string
rewrite_instance = Rewrite.from_json(json)
# print the JSON string representation of the object
print(Rewrite.to_json())

# convert the object into a dict
rewrite_dict = rewrite_instance.to_dict()
# create an instance of Rewrite from a dict
rewrite_from_dict = Rewrite.from_dict(rewrite_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


