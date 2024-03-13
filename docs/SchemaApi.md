# openapi_client.SchemaApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**schemas_list**](SchemaApi.md#schemas_list) | **POST** /v1/tenants/{tenant_id}/schemas/list | list all authorization models
[**schemas_read**](SchemaApi.md#schemas_read) | **POST** /v1/tenants/{tenant_id}/schemas/read | read your authorization model
[**schemas_write**](SchemaApi.md#schemas_write) | **POST** /v1/tenants/{tenant_id}/schemas/write | write your authorization model


# **schemas_list**
> SchemaListResponse schemas_list(tenant_id, body)

list all authorization models

### Example


```python
import openapi_client
from openapi_client.models.schema_list_response import SchemaListResponse
from openapi_client.models.schemas_list_request import SchemasListRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SchemaApi(api_client)
    tenant_id = 'tenant_id_example' # str | tenant_id is a string that identifies the tenant. It must match the pattern \"[a-zA-Z0-9-,]+\", be a maximum of 64 bytes, and must not be empty.
    body = openapi_client.SchemasListRequest() # SchemasListRequest | 

    try:
        # list all authorization models
        api_response = api_instance.schemas_list(tenant_id, body)
        print("The response of SchemaApi->schemas_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemaApi->schemas_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| tenant_id is a string that identifies the tenant. It must match the pattern \&quot;[a-zA-Z0-9-,]+\&quot;, be a maximum of 64 bytes, and must not be empty. | 
 **body** | [**SchemasListRequest**](SchemasListRequest.md)|  | 

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

# **schemas_read**
> SchemaReadResponse schemas_read(tenant_id, body)

read your authorization model

### Example


```python
import openapi_client
from openapi_client.models.schema_read_response import SchemaReadResponse
from openapi_client.models.schemas_read_request import SchemasReadRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SchemaApi(api_client)
    tenant_id = 'tenant_id_example' # str | tenant_id is a string that identifies the tenant. It must match the pattern \"[a-zA-Z0-9-,]+\", be a maximum of 64 bytes, and must not be empty.
    body = openapi_client.SchemasReadRequest() # SchemasReadRequest | 

    try:
        # read your authorization model
        api_response = api_instance.schemas_read(tenant_id, body)
        print("The response of SchemaApi->schemas_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemaApi->schemas_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| tenant_id is a string that identifies the tenant. It must match the pattern \&quot;[a-zA-Z0-9-,]+\&quot;, be a maximum of 64 bytes, and must not be empty. | 
 **body** | [**SchemasReadRequest**](SchemasReadRequest.md)|  | 

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

write your authorization model

### Example


```python
import openapi_client
from openapi_client.models.schema_write_response import SchemaWriteResponse
from openapi_client.models.schemas_write_request import SchemasWriteRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SchemaApi(api_client)
    tenant_id = 'tenant_id_example' # str | tenant_id is a string that identifies the tenant. It must match the pattern \"[a-zA-Z0-9-,]+\", be a maximum of 64 bytes, and must not be empty.
    body = openapi_client.SchemasWriteRequest() # SchemasWriteRequest | 

    try:
        # write your authorization model
        api_response = api_instance.schemas_write(tenant_id, body)
        print("The response of SchemaApi->schemas_write:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemaApi->schemas_write: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| tenant_id is a string that identifies the tenant. It must match the pattern \&quot;[a-zA-Z0-9-,]+\&quot;, be a maximum of 64 bytes, and must not be empty. | 
 **body** | [**SchemasWriteRequest**](SchemasWriteRequest.md)|  | 

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

