# SchemaWriteBody

SchemaWriteRequest is the request message for the Write method in the Schema service. It contains tenant_id and the schema to be written.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | schema is the string representation of the schema to be written. | [optional] 

## Example

```python
from permify.models.schema_write_body import SchemaWriteBody

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaWriteBody from a JSON string
schema_write_body_instance = SchemaWriteBody.from_json(json)
# print the JSON string representation of the object
print(SchemaWriteBody.to_json())

# convert the object into a dict
schema_write_body_dict = schema_write_body_instance.to_dict()
# create an instance of SchemaWriteBody from a dict
schema_write_body_from_dict = SchemaWriteBody.from_dict(schema_write_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


