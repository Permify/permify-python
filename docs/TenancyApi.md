# permify.TenancyApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tenants_create**](TenancyApi.md#tenants_create) | **POST** /v1/tenants/create | create new tenant
[**tenants_delete**](TenancyApi.md#tenants_delete) | **DELETE** /v1/tenants/{id} | delete tenant
[**tenants_list**](TenancyApi.md#tenants_list) | **POST** /v1/tenants/list | list tenants


# **tenants_create**
> TenantCreateResponse tenants_create(body)

create new tenant

### Example


```python
import permify
from permify.models.tenant_create_request import TenantCreateRequest
from permify.models.tenant_create_response import TenantCreateResponse
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
    api_instance = permify.TenancyApi(api_client)
    body = permify.TenantCreateRequest() # TenantCreateRequest | TenantCreateRequest is the message used for the request to create a tenant.

    try:
        # create new tenant
        api_response = api_instance.tenants_create(body)
        print("The response of TenancyApi->tenants_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenancyApi->tenants_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TenantCreateRequest**](TenantCreateRequest.md)| TenantCreateRequest is the message used for the request to create a tenant. | 

### Return type

[**TenantCreateResponse**](TenantCreateResponse.md)

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

# **tenants_delete**
> TenantDeleteResponse tenants_delete(id)

delete tenant

### Example


```python
import permify
from permify.models.tenant_delete_response import TenantDeleteResponse
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
    api_instance = permify.TenancyApi(api_client)
    id = 'id_example' # str | id is the unique identifier of the tenant to be deleted.

    try:
        # delete tenant
        api_response = api_instance.tenants_delete(id)
        print("The response of TenancyApi->tenants_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenancyApi->tenants_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id is the unique identifier of the tenant to be deleted. | 

### Return type

[**TenantDeleteResponse**](TenantDeleteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_list**
> TenantListResponse tenants_list(body)

list tenants

### Example


```python
import permify
from permify.models.tenant_list_request import TenantListRequest
from permify.models.tenant_list_response import TenantListResponse
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
    api_instance = permify.TenancyApi(api_client)
    body = permify.TenantListRequest() # TenantListRequest | TenantListRequest is the message used for the request to list all tenants.

    try:
        # list tenants
        api_response = api_instance.tenants_list(body)
        print("The response of TenancyApi->tenants_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenancyApi->tenants_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TenantListRequest**](TenantListRequest.md)| TenantListRequest is the message used for the request to list all tenants. | 

### Return type

[**TenantListResponse**](TenantListResponse.md)

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

