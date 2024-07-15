# permify.SchemaApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**schemas_list**](SchemaApi.md#schemas_list) | **POST** /v1/tenants/{tenant_id}/schemas/list | list schema
[**schemas_partial_write**](SchemaApi.md#schemas_partial_write) | **PATCH** /v1/tenants/{tenant_id}/schemas/partial-write | partially update your authorization model
[**schemas_read**](SchemaApi.md#schemas_read) | **POST** /v1/tenants/{tenant_id}/schemas/read | read schema
[**schemas_write**](SchemaApi.md#schemas_write) | **POST** /v1/tenants/{tenant_id}/schemas/write | write schema


# **schemas_list**
> SchemaListResponse schemas_list(tenant_id, body)

list schema

### Example


```python
import permify
from permify.models.schema_list_body import SchemaListBody
from permify.models.schema_list_response import SchemaListResponse
from permify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = permify.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with permify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = permify.SchemaApi(api_client)
    tenant_id = 'tenant_id_example' # str | Identifier of the tenant, if you are not using multi-tenancy (have only one tenant) use pre-inserted tenant <code>t1</code> for this field. Required, and must match the pattern \\“[a-zA-Z0-9-,]+\\“, max 64 bytes.
    body = permify.SchemaListBody() # SchemaListBody | 

    try:
        # list schema
        api_response = api_instance.schemas_list(tenant_id, body)
        print("The response of SchemaApi->schemas_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemaApi->schemas_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Identifier of the tenant, if you are not using multi-tenancy (have only one tenant) use pre-inserted tenant &lt;code&gt;t1&lt;/code&gt; for this field. Required, and must match the pattern \\“[a-zA-Z0-9-,]+\\“, max 64 bytes. | 
 **body** | [**SchemaListBody**](SchemaListBody.md)|  | 

### Return type

[**SchemaListResponse**](SchemaListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schemas_partial_write**
> SchemaPartialWriteResponse schemas_partial_write(tenant_id, body)

partially update your authorization model

### Example


```python
import permify
from permify.models.partial_write_body import PartialWriteBody
from permify.models.schema_partial_write_response import SchemaPartialWriteResponse
from permify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = permify.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with permify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = permify.SchemaApi(api_client)
    tenant_id = 'tenant_id_example' # str | tenant_id is a string that identifies the tenant. It must match the pattern \"[a-zA-Z0-9-,]+\", be a maximum of 64 bytes, and must not be empty.
    body = permify.PartialWriteBody() # PartialWriteBody | 

    try:
        # partially update your authorization model
        api_response = api_instance.schemas_partial_write(tenant_id, body)
        print("The response of SchemaApi->schemas_partial_write:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemaApi->schemas_partial_write: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| tenant_id is a string that identifies the tenant. It must match the pattern \&quot;[a-zA-Z0-9-,]+\&quot;, be a maximum of 64 bytes, and must not be empty. | 
 **body** | [**PartialWriteBody**](PartialWriteBody.md)|  | 

### Return type

[**SchemaPartialWriteResponse**](SchemaPartialWriteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schemas_read**
> SchemaReadResponse schemas_read(tenant_id, body)

read schema

### Example


```python
import permify
from permify.models.schema_read_body import SchemaReadBody
from permify.models.schema_read_response import SchemaReadResponse
from permify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = permify.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with permify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = permify.SchemaApi(api_client)
    tenant_id = 'tenant_id_example' # str | Identifier of the tenant, if you are not using multi-tenancy (have only one tenant) use pre-inserted tenant <code>t1</code> for this field. Required, and must match the pattern \\“[a-zA-Z0-9-,]+\\“, max 64 bytes.
    body = permify.SchemaReadBody() # SchemaReadBody | 

    try:
        # read schema
        api_response = api_instance.schemas_read(tenant_id, body)
        print("The response of SchemaApi->schemas_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemaApi->schemas_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Identifier of the tenant, if you are not using multi-tenancy (have only one tenant) use pre-inserted tenant &lt;code&gt;t1&lt;/code&gt; for this field. Required, and must match the pattern \\“[a-zA-Z0-9-,]+\\“, max 64 bytes. | 
 **body** | [**SchemaReadBody**](SchemaReadBody.md)|  | 

### Return type

[**SchemaReadResponse**](SchemaReadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schemas_write**
> SchemaWriteResponse schemas_write(tenant_id, body)

write schema

### Example


```python
import permify
from permify.models.schema_write_body import SchemaWriteBody
from permify.models.schema_write_response import SchemaWriteResponse
from permify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = permify.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with permify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = permify.SchemaApi(api_client)
    tenant_id = 'tenant_id_example' # str | Identifier of the tenant, if you are not using multi-tenancy (have only one tenant) use pre-inserted tenant <code>t1</code> for this field. Required, and must match the pattern \\“[a-zA-Z0-9-,]+\\“, max 64 bytes.
    body = permify.SchemaWriteBody() # SchemaWriteBody | 

    try:
        # write schema
        api_response = api_instance.schemas_write(tenant_id, body)
        print("The response of SchemaApi->schemas_write:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemaApi->schemas_write: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Identifier of the tenant, if you are not using multi-tenancy (have only one tenant) use pre-inserted tenant &lt;code&gt;t1&lt;/code&gt; for this field. Required, and must match the pattern \\“[a-zA-Z0-9-,]+\\“, max 64 bytes. | 
 **body** | [**SchemaWriteBody**](SchemaWriteBody.md)|  | 

### Return type

[**SchemaWriteResponse**](SchemaWriteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

