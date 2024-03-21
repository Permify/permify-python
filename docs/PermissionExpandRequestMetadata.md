# PermissionExpandRequestMetadata

PermissionExpandRequestMetadata metadata for the PermissionExpandRequest.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** | Version of the schema. | [optional] 
**snap_token** | **str** | The snap token to avoid stale cache, see more details on [Snap Tokens](../../operations/snap-tokens). | [optional] 

## Example

```python
from permify.models.permission_expand_request_metadata import PermissionExpandRequestMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionExpandRequestMetadata from a JSON string
permission_expand_request_metadata_instance = PermissionExpandRequestMetadata.from_json(json)
# print the JSON string representation of the object
print(PermissionExpandRequestMetadata.to_json())

# convert the object into a dict
permission_expand_request_metadata_dict = permission_expand_request_metadata_instance.to_dict()
# create an instance of PermissionExpandRequestMetadata from a dict
permission_expand_request_metadata_form_dict = permission_expand_request_metadata.from_dict(permission_expand_request_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


