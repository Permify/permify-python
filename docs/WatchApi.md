# permify.WatchApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**watch_watch**](WatchApi.md#watch_watch) | **POST** /v1/tenants/{tenant_id}/watch | watch changes


# **watch_watch**
> StreamResultOfWatchResponse watch_watch(tenant_id, body)

watch changes

### Example


```python
import permify
from permify.models.stream_result_of_watch_response import StreamResultOfWatchResponse
from permify.models.watch_watch_request import WatchWatchRequest
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
    api_instance = permify.WatchApi(api_client)
    tenant_id = 'tenant_id_example' # str | Identifier of the tenant, if you are not using multi-tenancy (have only one tenant) use pre-inserted tenant <code>t1</code> for this field. Required, and must match the pattern \\“[a-zA-Z0-9-,]+\\“, max 64 bytes.
    body = permify.WatchWatchRequest() # WatchWatchRequest | 

    try:
        # watch changes
        api_response = api_instance.watch_watch(tenant_id, body)
        print("The response of WatchApi->watch_watch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WatchApi->watch_watch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Identifier of the tenant, if you are not using multi-tenancy (have only one tenant) use pre-inserted tenant &lt;code&gt;t1&lt;/code&gt; for this field. Required, and must match the pattern \\“[a-zA-Z0-9-,]+\\“, max 64 bytes. | 
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

