# PermissionLookupSubjectRequestMetadata

PermissionLookupSubjectRequestMetadata metadata for the PermissionLookupSubjectRequest.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** | Version of the schema. | [optional] 
**snap_token** | **str** | The snap token to avoid stale cache, see more details on [Snap Tokens](../../operations/snap-tokens). | [optional] 
**depth** | **int** | Query limit when if recursive database queries got in loop. | [optional] 

## Example

```python
from permify.models.permission_lookup_subject_request_metadata import PermissionLookupSubjectRequestMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionLookupSubjectRequestMetadata from a JSON string
permission_lookup_subject_request_metadata_instance = PermissionLookupSubjectRequestMetadata.from_json(json)
# print the JSON string representation of the object
print(PermissionLookupSubjectRequestMetadata.to_json())

# convert the object into a dict
permission_lookup_subject_request_metadata_dict = permission_lookup_subject_request_metadata_instance.to_dict()
# create an instance of PermissionLookupSubjectRequestMetadata from a dict
permission_lookup_subject_request_metadata_from_dict = PermissionLookupSubjectRequestMetadata.from_dict(permission_lookup_subject_request_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


