# openapi_client.WatchApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**watch_watch**](WatchApi.md#watch_watch) | **POST** /v1/tenants/{tenant_id}/watch | 


# **watch_watch**
> StreamResultOfWatchResponse watch_watch(tenant_id, body)



### Example


```python
import openapi_client
from openapi_client.models.stream_result_of_watch_response import StreamResultOfWatchResponse
from openapi_client.models.watch_watch_request import WatchWatchRequest
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
    api_instance = openapi_client.WatchApi(api_client)
    tenant_id = 'tenant_id_example' # str | Identifier of the tenant, required, and must match the pattern \"[a-zA-Z0-9-,]+\", max 64 bytes.
    body = openapi_client.WatchWatchRequest() # WatchWatchRequest | 

    try:
        api_response = api_instance.watch_watch(tenant_id, body)
        print("The response of WatchApi->watch_watch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WatchApi->watch_watch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Identifier of the tenant, required, and must match the pattern \&quot;[a-zA-Z0-9-,]+\&quot;, max 64 bytes. | 
 **body** | [**WatchWatchRequest**](WatchWatchRequest.md)|  | 

### Return type

[**StreamResultOfWatchResponse**](StreamResultOfWatchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response.(streaming responses) |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

