# SourceInfo

Source information collected at parse time.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**syntax_version** | **str** | The syntax version of the source, e.g. &#x60;cel1&#x60;. | [optional] 
**location** | **str** | The location name. All position information attached to an expression is relative to this location.  The location could be a file, UI element, or similar. For example, &#x60;acme/app/AnvilPolicy.cel&#x60;. | [optional] 
**line_offsets** | **List[int]** | Monotonically increasing list of code point offsets where newlines &#x60;\\n&#x60; appear.  The line number of a given position is the index &#x60;i&#x60; where for a given &#x60;id&#x60; the &#x60;line_offsets[i] &lt; id_positions[id] &lt; line_offsets[i+1]&#x60;. The column may be derivd from &#x60;id_positions[id] - line_offsets[i]&#x60;. | [optional] 
**positions** | **Dict[str, int]** | A map from the parse node id (e.g. &#x60;Expr.id&#x60;) to the code point offset within the source. | [optional] 
**macro_calls** | [**Dict[str, Expr]**](Expr.md) | A map from the parse node id where a macro replacement was made to the call &#x60;Expr&#x60; that resulted in a macro expansion.  For example, &#x60;has(value.field)&#x60; is a function call that is replaced by a &#x60;test_only&#x60; field selection in the AST. Likewise, the call &#x60;list.exists(e, e &gt; 10)&#x60; translates to a comprehension expression. The key in the map corresponds to the expression id of the expanded macro, and the value is the call &#x60;Expr&#x60; that was replaced. | [optional] 

## Example

```python
from openapi_client.models.source_info import SourceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SourceInfo from a JSON string
source_info_instance = SourceInfo.from_json(json)
# print the JSON string representation of the object
print(SourceInfo.to_json())

# convert the object into a dict
source_info_dict = source_info_instance.to_dict()
# create an instance of SourceInfo from a dict
source_info_form_dict = source_info.from_dict(source_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


