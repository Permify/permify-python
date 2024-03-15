# permify.BundleApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bundle_delete**](BundleApi.md#bundle_delete) | **POST** /v1/tenants/{tenant_id}/bundle/delete | delete bundle
[**bundle_read**](BundleApi.md#bundle_read) | **POST** /v1/tenants/{tenant_id}/bundle/read | read bundle
[**bundle_write**](BundleApi.md#bundle_write) | **POST** /v1/tenants/{tenant_id}/bundle/write | write bundle


# **bundle_delete**
> BundleDeleteResponse bundle_delete(tenant_id, body)

delete bundle

The \"Delete Bundle\" API is designed for removing specific data bundles within a multi-tenant application environment. This API facilitates the deletion of a bundle, identified by its unique name, from a designated tenant's environment.

### Example


```python
import permify
from permify.models.bundle_delete_request import BundleDeleteRequest
from permify.models.bundle_delete_response import BundleDeleteResponse
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
    api_instance = permify.BundleApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    body = permify.BundleDeleteRequest() # BundleDeleteRequest | 

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

The \"Read Bundle\" API is a crucial tool for retrieving details of specific data bundles in a multi-tenant application setup. It is designed to access information about a bundle, uniquely identified by its name, within the specified tenant's environment.

### Example


```python
import permify
from permify.models.bundle_read_request import BundleReadRequest
from permify.models.bundle_read_response import BundleReadResponse
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
    api_instance = permify.BundleApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    body = permify.BundleReadRequest() # BundleReadRequest | 

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

The \"Write Bundle\" API is designed for handling data in a multi-tenant application environment. Its primary function is to write and delete data according to predefined structures. This API allows users to define or update data bundles, each distinguished by a unique name.

### Example


```python
import permify
from permify.models.bundle_write_request import BundleWriteRequest
from permify.models.bundle_write_response import BundleWriteResponse
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
    api_instance = permify.BundleApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    body = permify.BundleWriteRequest() # BundleWriteRequest | 

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

