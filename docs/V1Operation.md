# V1Operation

Operation is a message representing a series of operations that can be performed. It includes fields for writing and deleting relationships and attributes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relationships_write** | **List[str]** | &#39;relationships_write&#39; is a repeated string field for storing relationship keys that are to be written or created. | [optional] 
**relationships_delete** | **List[str]** | &#39;relationships_delete&#39; is a repeated string field for storing relationship keys that are to be deleted or removed. | [optional] 
**attributes_write** | **List[str]** | &#39;attributes_write&#39; is a repeated string field for storing attribute keys that are to be written or created. | [optional] 
**attributes_delete** | **List[str]** | &#39;attributes_delete&#39; is a repeated string field for storing attribute keys that are to be deleted or removed. | [optional] 

## Example

```python
from permify.models.v1_operation import V1Operation

# TODO update the JSON string below
json = "{}"
# create an instance of V1Operation from a JSON string
v1_operation_instance = V1Operation.from_json(json)
# print the JSON string representation of the object
print(V1Operation.to_json())

# convert the object into a dict
v1_operation_dict = v1_operation_instance.to_dict()
# create an instance of V1Operation from a dict
v1_operation_form_dict = v1_operation.from_dict(v1_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


