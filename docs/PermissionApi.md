# permify.PermissionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**permissions_check**](PermissionApi.md#permissions_check) | **POST** /v1/tenants/{tenant_id}/permissions/check | This method returns a decision about whether user can perform an permission on a certain resource.
[**permissions_expand**](PermissionApi.md#permissions_expand) | **POST** /v1/tenants/{tenant_id}/permissions/expand | expand relationships according to schema
[**permissions_lookup_entity**](PermissionApi.md#permissions_lookup_entity) | **POST** /v1/tenants/{tenant_id}/permissions/lookup-entity | Retrieve an entity by its identifier.
[**permissions_lookup_entity_stream**](PermissionApi.md#permissions_lookup_entity_stream) | **POST** /v1/tenants/{tenant_id}/permissions/lookup-entity-stream | Stream entities by their identifiers.
[**permissions_lookup_subject**](PermissionApi.md#permissions_lookup_subject) | **POST** /v1/tenants/{tenant_id}/permissions/lookup-subject | Retrieve a subject by its identifier.
[**permissions_subject_permission**](PermissionApi.md#permissions_subject_permission) | **POST** /v1/tenants/{tenant_id}/permissions/subject-permission | Retrieve permissions related to a specific subject.


# **permissions_check**
> PermissionCheckResponse permissions_check(tenant_id, body)

This method returns a decision about whether user can perform an permission on a certain resource.

### Example


```python
import permify
from permify.models.permission_check_response import PermissionCheckResponse
from permify.models.permissions_check_request import PermissionsCheckRequest
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
    api_instance = permify.PermissionApi(api_client)
    tenant_id = 'tenant_id_example' # str | Identifier of the tenant, required, and must match the pattern \"[a-zA-Z0-9-,]+\", max 64 bytes.
    body = permify.PermissionsCheckRequest() # PermissionsCheckRequest | 

    try:
        # This method returns a decision about whether user can perform an permission on a certain resource.
        api_response = api_instance.permissions_check(tenant_id, body)
        print("The response of PermissionApi->permissions_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionApi->permissions_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Identifier of the tenant, required, and must match the pattern \&quot;[a-zA-Z0-9-,]+\&quot;, max 64 bytes. | 
 **body** | [**PermissionsCheckRequest**](PermissionsCheckRequest.md)|  | 

### Return type

[**PermissionCheckResponse**](PermissionCheckResponse.md)

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

# **permissions_expand**
> PermissionExpandResponse permissions_expand(tenant_id, body)

expand relationships according to schema

### Example


```python
import permify
from permify.models.permission_expand_response import PermissionExpandResponse
from permify.models.permissions_expand_request import PermissionsExpandRequest
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
    api_instance = permify.PermissionApi(api_client)
    tenant_id = 'tenant_id_example' # str | Identifier of the tenant, required, and must match the pattern \"[a-zA-Z0-9-,]+\", max 64 bytes.
    body = permify.PermissionsExpandRequest() # PermissionsExpandRequest | 

    try:
        # expand relationships according to schema
        api_response = api_instance.permissions_expand(tenant_id, body)
        print("The response of PermissionApi->permissions_expand:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionApi->permissions_expand: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Identifier of the tenant, required, and must match the pattern \&quot;[a-zA-Z0-9-,]+\&quot;, max 64 bytes. | 
 **body** | [**PermissionsExpandRequest**](PermissionsExpandRequest.md)|  | 

### Return type

[**PermissionExpandResponse**](PermissionExpandResponse.md)

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

# **permissions_lookup_entity**
> PermissionLookupEntityResponse permissions_lookup_entity(tenant_id, body)

Retrieve an entity by its identifier.

### Example


```python
import permify
from permify.models.permission_lookup_entity_response import PermissionLookupEntityResponse
from permify.models.permissions_lookup_entity_request import PermissionsLookupEntityRequest
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
    api_instance = permify.PermissionApi(api_client)
    tenant_id = 'tenant_id_example' # str | Identifier of the tenant, required, and must match the pattern \"[a-zA-Z0-9-,]+\", max 64 bytes.
    body = permify.PermissionsLookupEntityRequest() # PermissionsLookupEntityRequest | 

    try:
        # Retrieve an entity by its identifier.
        api_response = api_instance.permissions_lookup_entity(tenant_id, body)
        print("The response of PermissionApi->permissions_lookup_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionApi->permissions_lookup_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Identifier of the tenant, required, and must match the pattern \&quot;[a-zA-Z0-9-,]+\&quot;, max 64 bytes. | 
 **body** | [**PermissionsLookupEntityRequest**](PermissionsLookupEntityRequest.md)|  | 

### Return type

[**PermissionLookupEntityResponse**](PermissionLookupEntityResponse.md)

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

# **permissions_lookup_entity_stream**
> StreamResultOfPermissionLookupEntityStreamResponse permissions_lookup_entity_stream(tenant_id, body)

Stream entities by their identifiers.

### Example


```python
import permify
from permify.models.permissions_lookup_entity_request import PermissionsLookupEntityRequest
from permify.models.stream_result_of_permission_lookup_entity_stream_response import StreamResultOfPermissionLookupEntityStreamResponse
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
    api_instance = permify.PermissionApi(api_client)
    tenant_id = 'tenant_id_example' # str | Identifier of the tenant, required, and must match the pattern \"[a-zA-Z0-9-,]+\", max 64 bytes.
    body = permify.PermissionsLookupEntityRequest() # PermissionsLookupEntityRequest | 

    try:
        # Stream entities by their identifiers.
        api_response = api_instance.permissions_lookup_entity_stream(tenant_id, body)
        print("The response of PermissionApi->permissions_lookup_entity_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionApi->permissions_lookup_entity_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Identifier of the tenant, required, and must match the pattern \&quot;[a-zA-Z0-9-,]+\&quot;, max 64 bytes. | 
 **body** | [**PermissionsLookupEntityRequest**](PermissionsLookupEntityRequest.md)|  | 

### Return type

[**StreamResultOfPermissionLookupEntityStreamResponse**](StreamResultOfPermissionLookupEntityStreamResponse.md)

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

# **permissions_lookup_subject**
> PermissionLookupSubjectResponse permissions_lookup_subject(tenant_id, body)

Retrieve a subject by its identifier.

### Example


```python
import permify
from permify.models.permission_lookup_subject_response import PermissionLookupSubjectResponse
from permify.models.permissions_lookup_subject_request import PermissionsLookupSubjectRequest
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
    api_instance = permify.PermissionApi(api_client)
    tenant_id = 'tenant_id_example' # str | Identifier of the tenant, required, and must match the pattern \"[a-zA-Z0-9-,]+\", max 64 bytes.
    body = permify.PermissionsLookupSubjectRequest() # PermissionsLookupSubjectRequest | 

    try:
        # Retrieve a subject by its identifier.
        api_response = api_instance.permissions_lookup_subject(tenant_id, body)
        print("The response of PermissionApi->permissions_lookup_subject:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionApi->permissions_lookup_subject: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Identifier of the tenant, required, and must match the pattern \&quot;[a-zA-Z0-9-,]+\&quot;, max 64 bytes. | 
 **body** | [**PermissionsLookupSubjectRequest**](PermissionsLookupSubjectRequest.md)|  | 

### Return type

[**PermissionLookupSubjectResponse**](PermissionLookupSubjectResponse.md)

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

# **permissions_subject_permission**
> PermissionSubjectPermissionResponse permissions_subject_permission(tenant_id, body)

Retrieve permissions related to a specific subject.

### Example


```python
import permify
from permify.models.permission_subject_permission_response import PermissionSubjectPermissionResponse
from permify.models.permissions_subject_permission_request import PermissionsSubjectPermissionRequest
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
    api_instance = permify.PermissionApi(api_client)
    tenant_id = 'tenant_id_example' # str | Identifier of the tenant, required, and must match the pattern \"[a-zA-Z0-9-,]+\", max 64 bytes.
    body = permify.PermissionsSubjectPermissionRequest() # PermissionsSubjectPermissionRequest | 

    try:
        # Retrieve permissions related to a specific subject.
        api_response = api_instance.permissions_subject_permission(tenant_id, body)
        print("The response of PermissionApi->permissions_subject_permission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionApi->permissions_subject_permission: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Identifier of the tenant, required, and must match the pattern \&quot;[a-zA-Z0-9-,]+\&quot;, max 64 bytes. | 
 **body** | [**PermissionsSubjectPermissionRequest**](PermissionsSubjectPermissionRequest.md)|  | 

### Return type

[**PermissionSubjectPermissionResponse**](PermissionSubjectPermissionResponse.md)

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

