# PermissionCheckRequestMetadata

PermissionCheckRequestMetadata is the metadata associated with a PermissionCheckRequest.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** | Version of the schema. | [optional] 
**snap_token** | **str** | Token associated with the snap. | [optional] 
**depth** | **int** | Depth of the check, must be greater than or equal to 3. | [optional] 

## Example

```python
from permify.models.permission_check_request_metadata import PermissionCheckRequestMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionCheckRequestMetadata from a JSON string
permission_check_request_metadata_instance = PermissionCheckRequestMetadata.from_json(json)
# print the JSON string representation of the object
print(PermissionCheckRequestMetadata.to_json())

# convert the object into a dict
permission_check_request_metadata_dict = permission_check_request_metadata_instance.to_dict()
# create an instance of PermissionCheckRequestMetadata from a dict
permission_check_request_metadata_form_dict = permission_check_request_metadata.from_dict(permission_check_request_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


