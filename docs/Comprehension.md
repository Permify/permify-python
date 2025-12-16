# Comprehension

A comprehension expression applied to a list or map.  Comprehensions are not part of the core syntax, but enabled with macros. A macro matches a specific call signature within a parsed AST and replaces the call with an alternate AST block. Macro expansion happens at parse time.  The following macros are supported within CEL:  Aggregate type macros may be applied to all elements in a list or all keys in a map:  *  `all`, `exists`, `exists_one` -  test a predicate expression against    the inputs and return `true` if the predicate is satisfied for all,    any, or only one value `list.all(x, x < 10)`. *  `filter` - test a predicate expression against the inputs and return    the subset of elements which satisfy the predicate:    `payments.filter(p, p > 1000)`. *  `map` - apply an expression to all elements in the input and return the    output aggregate type: `[1, 2, 3].map(i, i * i)`.  The `has(m.x)` macro tests whether the property `x` is present in struct `m`. The semantics of this macro depend on the type of `m`. For proto2 messages `has(m.x)` is defined as 'defined, but not set`. For proto3, the macro tests whether the property is set to its default. For map and struct types, the macro tests whether the property `x` is defined on `m`.  Comprehensions for the standard environment macros evaluation can be best visualized as the following pseudocode:  ``` let `accu_var` = `accu_init` for (let `iter_var` in `iter_range`) {   if (!`loop_condition`) {     break   }   `accu_var` = `loop_step` } return `result` ```  Comprehensions for the optional V2 macros which support map-to-map translation differ slightly from the standard environment macros in that they expose both the key or index in addition to the value for each list or map entry:  ``` let `accu_var` = `accu_init` for (let `iter_var`, `iter_var2` in `iter_range`) {   if (!`loop_condition`) {     break   }   `accu_var` = `loop_step` } return `result` ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iter_var** | **str** | The name of the first iteration variable. When the iter_range is a list, this variable is the list element. When the iter_range is a map, this variable is the map entry key. | [optional] 
**iter_var2** | **str** | The name of the second iteration variable, empty if not set. When the iter_range is a list, this variable is the integer index. When the iter_range is a map, this variable is the map entry value. This field is only set for comprehension v2 macros. | [optional] 
**iter_range** | [**Expr**](Expr.md) |  | [optional] 
**accu_var** | **str** | The name of the variable used for accumulation of the result. | [optional] 
**accu_init** | [**Expr**](Expr.md) |  | [optional] 
**loop_condition** | [**Expr**](Expr.md) |  | [optional] 
**loop_step** | [**Expr**](Expr.md) |  | [optional] 
**result** | [**Expr**](Expr.md) |  | [optional] 

## Example

```python
from permify.models.comprehension import Comprehension

# TODO update the JSON string below
json = "{}"
# create an instance of Comprehension from a JSON string
comprehension_instance = Comprehension.from_json(json)
# print the JSON string representation of the object
print Comprehension.to_json()

# convert the object into a dict
comprehension_dict = comprehension_instance.to_dict()
# create an instance of Comprehension from a dict
comprehension_form_dict = comprehension.from_dict(comprehension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


