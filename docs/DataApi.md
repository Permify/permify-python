# openapi_client.DataApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bundle_run**](DataApi.md#bundle_run) | **POST** /v1/tenants/{tenant_id}/data/run-bundle | run bundle
[**data_attributes_read**](DataApi.md#data_attributes_read) | **POST** /v1/tenants/{tenant_id}/data/attributes/read | read attribute(s)
[**data_delete**](DataApi.md#data_delete) | **POST** /v1/tenants/{tenant_id}/data/delete | delete data
[**data_relationships_read**](DataApi.md#data_relationships_read) | **POST** /v1/tenants/{tenant_id}/data/relationships/read | read relation tuple(s)
[**data_write**](DataApi.md#data_write) | **POST** /v1/tenants/{tenant_id}/data/write | create data
[**relationships_delete**](DataApi.md#relationships_delete) | **POST** /v1/tenants/{tenant_id}/relationships/delete | delete relationships
[**relationships_write**](DataApi.md#relationships_write) | **POST** /v1/tenants/{tenant_id}/relationships/write | create new relationships


# **bundle_run**
> BundleRunResponse bundle_run(tenant_id, body)

run bundle

### Example


```python
import openapi_client
from openapi_client.models.bundle_run_request import BundleRunRequest
from openapi_client.models.bundle_run_response import BundleRunResponse
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
    api_instance = openapi_client.DataApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    body = openapi_client.BundleRunRequest() # BundleRunRequest | 

    try:
        # run bundle
        api_response = api_instance.bundle_run(tenant_id, body)
        print("The response of DataApi->bundle_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->bundle_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **body** | [**BundleRunRequest**](BundleRunRequest.md)|  | 

### Return type

[**BundleRunResponse**](BundleRunResponse.md)

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

# **data_attributes_read**
> AttributeReadResponse data_attributes_read(tenant_id, body)

read attribute(s)

### Example


```python
import openapi_client
from openapi_client.models.attribute_read_response import AttributeReadResponse
from openapi_client.models.data_attributes_read_request import DataAttributesReadRequest
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
    api_instance = openapi_client.DataApi(api_client)
    tenant_id = 'tenant_id_example' # str | tenant_id represents the unique identifier of the tenant from which the attributes are being read.
    body = openapi_client.DataAttributesReadRequest() # DataAttributesReadRequest | 

    try:
        # read attribute(s)
        api_response = api_instance.data_attributes_read(tenant_id, body)
        print("The response of DataApi->data_attributes_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->data_attributes_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| tenant_id represents the unique identifier of the tenant from which the attributes are being read. | 
 **body** | [**DataAttributesReadRequest**](DataAttributesReadRequest.md)|  | 

### Return type

[**AttributeReadResponse**](AttributeReadResponse.md)

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

# **data_delete**
> DataDeleteResponse data_delete(tenant_id, body)

delete data

### Example


```python
import openapi_client
from openapi_client.models.data_delete_request import DataDeleteRequest
from openapi_client.models.data_delete_response import DataDeleteResponse
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
    api_instance = openapi_client.DataApi(api_client)
    tenant_id = 'tenant_id_example' # str | tenant_id represents the unique identifier of the tenant from which the data will be deleted.
    body = openapi_client.DataDeleteRequest() # DataDeleteRequest | 

    try:
        # delete data
        api_response = api_instance.data_delete(tenant_id, body)
        print("The response of DataApi->data_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->data_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| tenant_id represents the unique identifier of the tenant from which the data will be deleted. | 
 **body** | [**DataDeleteRequest**](DataDeleteRequest.md)|  | 

### Return type

[**DataDeleteResponse**](DataDeleteResponse.md)

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

# **data_relationships_read**
> RelationshipReadResponse data_relationships_read(tenant_id, body)

read relation tuple(s)

### Example


```python
import openapi_client
from openapi_client.models.data_relationships_read_request import DataRelationshipsReadRequest
from openapi_client.models.relationship_read_response import RelationshipReadResponse
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
    api_instance = openapi_client.DataApi(api_client)
    tenant_id = 'tenant_id_example' # str | tenant_id represents the unique identifier of the tenant for which relationships are read.
    body = openapi_client.DataRelationshipsReadRequest() # DataRelationshipsReadRequest | 

    try:
        # read relation tuple(s)
        api_response = api_instance.data_relationships_read(tenant_id, body)
        print("The response of DataApi->data_relationships_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->data_relationships_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| tenant_id represents the unique identifier of the tenant for which relationships are read. | 
 **body** | [**DataRelationshipsReadRequest**](DataRelationshipsReadRequest.md)|  | 

### Return type

[**RelationshipReadResponse**](RelationshipReadResponse.md)

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

# **data_write**
> DataWriteResponse data_write(tenant_id, body)

create data

### Example


```python
import openapi_client
from openapi_client.models.data_write_request import DataWriteRequest
from openapi_client.models.data_write_response import DataWriteResponse
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
    api_instance = openapi_client.DataApi(api_client)
    tenant_id = 'tenant_id_example' # str | tenant_id represents the unique identifier of the tenant for which data is written.
    body = openapi_client.DataWriteRequest() # DataWriteRequest | 

    try:
        # create data
        api_response = api_instance.data_write(tenant_id, body)
        print("The response of DataApi->data_write:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->data_write: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| tenant_id represents the unique identifier of the tenant for which data is written. | 
 **body** | [**DataWriteRequest**](DataWriteRequest.md)|  | 

### Return type

[**DataWriteResponse**](DataWriteResponse.md)

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

# **relationships_delete**
> RelationshipDeleteResponse relationships_delete(tenant_id, body)

delete relationships

### Example


```python
import openapi_client
from openapi_client.models.relationship_delete_request import RelationshipDeleteRequest
from openapi_client.models.relationship_delete_response import RelationshipDeleteResponse
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
    api_instance = openapi_client.DataApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    body = openapi_client.RelationshipDeleteRequest() # RelationshipDeleteRequest | 

    try:
        # delete relationships
        api_response = api_instance.relationships_delete(tenant_id, body)
        print("The response of DataApi->relationships_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->relationships_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **body** | [**RelationshipDeleteRequest**](RelationshipDeleteRequest.md)|  | 

### Return type

[**RelationshipDeleteResponse**](RelationshipDeleteResponse.md)

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

# **relationships_write**
> RelationshipWriteResponse relationships_write(tenant_id, body)

create new relationships

### Example


```python
import openapi_client
from openapi_client.models.relationship_write_response import RelationshipWriteResponse
from openapi_client.models.relationships_write_request import RelationshipsWriteRequest
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
    api_instance = openapi_client.DataApi(api_client)
    tenant_id = 'tenant_id_example' # str | Unique identifier for the tenant with specific constraints.
    body = openapi_client.RelationshipsWriteRequest() # RelationshipsWriteRequest | 

    try:
        # create new relationships
        api_response = api_instance.relationships_write(tenant_id, body)
        print("The response of DataApi->relationships_write:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->relationships_write: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Unique identifier for the tenant with specific constraints. | 
 **body** | [**RelationshipsWriteRequest**](RelationshipsWriteRequest.md)|  | 

### Return type

[**RelationshipWriteResponse**](RelationshipWriteResponse.md)

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

