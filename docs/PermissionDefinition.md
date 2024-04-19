# PermissionDefinition

The PermissionDefinition message provides detailed information about a specific permission.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the permission, which follows a specific string pattern and has a maximum byte size. | [optional] 
**child** | [**Child**](Child.md) |  | [optional] 

## Example

```python
from permify.models.permission_definition import PermissionDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionDefinition from a JSON string
permission_definition_instance = PermissionDefinition.from_json(json)
# print the JSON string representation of the object
print(PermissionDefinition.to_json())

# convert the object into a dict
permission_definition_dict = permission_definition_instance.to_dict()
# create an instance of PermissionDefinition from a dict
permission_definition_from_dict = PermissionDefinition.from_dict(permission_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


