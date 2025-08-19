# CheckBody

PermissionCheckRequest is the request message for the Check method in the Permission service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**PermissionCheckRequestMetadata**](PermissionCheckRequestMetadata.md) |  | [optional] 
**entity** | [**Entity**](Entity.md) |  | [optional] 
**permission** | **str** | The action the user wants to perform on the resource | [optional] 
**subject** | [**Subject**](Subject.md) |  | [optional] 
**context** | [**Context**](Context.md) |  | [optional] 
**arguments** | [**List[Argument]**](Argument.md) | Additional arguments associated with this request. | [optional] 

## Example

```python
from permify.models.check_body import CheckBody

# TODO update the JSON string below
json = "{}"
# create an instance of CheckBody from a JSON string
check_body_instance = CheckBody.from_json(json)
# print the JSON string representation of the object
print CheckBody.to_json()

# convert the object into a dict
check_body_dict = check_body_instance.to_dict()
# create an instance of CheckBody from a dict
check_body_form_dict = check_body.from_dict(check_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


