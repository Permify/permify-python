# PermissionCheckResponseMetadata

PermissionCheckResponseMetadata is the metadata associated with a PermissionCheckResponse.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_count** | **int** | The count of the checks performed. | [optional] 

## Example

```python
from openapi_client.models.permission_check_response_metadata import PermissionCheckResponseMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionCheckResponseMetadata from a JSON string
permission_check_response_metadata_instance = PermissionCheckResponseMetadata.from_json(json)
# print the JSON string representation of the object
print(PermissionCheckResponseMetadata.to_json())

# convert the object into a dict
permission_check_response_metadata_dict = permission_check_response_metadata_instance.to_dict()
# create an instance of PermissionCheckResponseMetadata from a dict
permission_check_response_metadata_form_dict = permission_check_response_metadata.from_dict(permission_check_response_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


