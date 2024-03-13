# openapi_client.BundleApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bundle_delete**](BundleApi.md#bundle_delete) | **POST** /v1/tenants/{tenant_id}/bundle/delete | delete bundle
[**bundle_read**](BundleApi.md#bundle_read) | **POST** /v1/tenants/{tenant_id}/bundle/read | read bundle
[**bundle_write**](BundleApi.md#bundle_write) | **POST** /v1/tenants/{tenant_id}/bundle/write | write bundle


# **bundle_delete**
> BundleDeleteResponse bundle_delete(tenant_id, body)

delete bundle

### Example


```python
import openapi_client
from openapi_client.models.bundle_delete_request import BundleDeleteRequest
from openapi_client.models.bundle_delete_response import BundleDeleteResponse
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
    api_instance = openapi_client.BundleApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    body = openapi_client.BundleDeleteRequest() # BundleDeleteRequest | 

    try:
        # delete bundle
        api_response = api_instance.bundle_delete(tenant_id, body)
        print("The response of BundleApi->bundle_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BundleApi->bundle_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **body** | [**BundleDeleteRequest**](BundleDeleteRequest.md)|  | 

### Return type

[**BundleDeleteResponse**](BundleDeleteResponse.md)

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

# **bundle_read**
> BundleReadResponse bundle_read(tenant_id, body)

read bundle

### Example


```python
import openapi_client
from openapi_client.models.bundle_read_request import BundleReadRequest
from openapi_client.models.bundle_read_response import BundleReadResponse
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
    api_instance = openapi_client.BundleApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    body = openapi_client.BundleReadRequest() # BundleReadRequest | 

    try:
        # read bundle
        api_response = api_instance.bundle_read(tenant_id, body)
        print("The response of BundleApi->bundle_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BundleApi->bundle_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **body** | [**BundleReadRequest**](BundleReadRequest.md)|  | 

### Return type

[**BundleReadResponse**](BundleReadResponse.md)

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

# **bundle_write**
> BundleWriteResponse bundle_write(tenant_id, body)

write bundle

### Example


```python
import openapi_client
from openapi_client.models.bundle_write_request import BundleWriteRequest
from openapi_client.models.bundle_write_response import BundleWriteResponse
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
    api_instance = openapi_client.BundleApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    body = openapi_client.BundleWriteRequest() # BundleWriteRequest | 

    try:
        # write bundle
        api_response = api_instance.bundle_write(tenant_id, body)
        print("The response of BundleApi->bundle_write:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BundleApi->bundle_write: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **body** | [**BundleWriteRequest**](BundleWriteRequest.md)|  | 

### Return type

[**BundleWriteResponse**](BundleWriteResponse.md)

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

