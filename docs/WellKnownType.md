# WellKnownType

Well-known protobuf types treated with first-class support in CEL.   - ANY: Well-known protobuf.Any type.  Any types are a polymorphic message type. During type-checking they are treated like `DYN` types, but at runtime they are resolved to a specific message type specified at evaluation time.  - TIMESTAMP: Well-known protobuf.Timestamp type, internally referenced as `timestamp`.  - DURATION: Well-known protobuf.Duration type, internally referenced as `duration`.

## Enum

* `ANY` (value: `'ANY'`)

* `TIMESTAMP` (value: `'TIMESTAMP'`)

* `DURATION` (value: `'DURATION'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


