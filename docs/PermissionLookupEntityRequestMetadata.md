# PermissionLookupEntityRequestMetadata

PermissionLookupEntityRequestMetadata is the metadata associated with a PermissionLookupEntityRequest.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** | Version of the schema. | [optional] 
**snap_token** | **str** | Token associated with the snap. | [optional] 
**depth** | **int** | Depth of lookup, required, must be greater or equal to 3. | [optional] 

## Example

```python
from permify.models.permission_lookup_entity_request_metadata import PermissionLookupEntityRequestMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionLookupEntityRequestMetadata from a JSON string
permission_lookup_entity_request_metadata_instance = PermissionLookupEntityRequestMetadata.from_json(json)
# print the JSON string representation of the object
print(PermissionLookupEntityRequestMetadata.to_json())

# convert the object into a dict
permission_lookup_entity_request_metadata_dict = permission_lookup_entity_request_metadata_instance.to_dict()
# create an instance of PermissionLookupEntityRequestMetadata from a dict
permission_lookup_entity_request_metadata_form_dict = permission_lookup_entity_request_metadata.from_dict(permission_lookup_entity_request_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


