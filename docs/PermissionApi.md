# permify.PermissionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**permissions_check**](PermissionApi.md#permissions_check) | **POST** /v1/tenants/{tenant_id}/permissions/check | check api
[**permissions_expand**](PermissionApi.md#permissions_expand) | **POST** /v1/tenants/{tenant_id}/permissions/expand | expand api
[**permissions_lookup_entity**](PermissionApi.md#permissions_lookup_entity) | **POST** /v1/tenants/{tenant_id}/permissions/lookup-entity | lookup entity
[**permissions_lookup_entity_stream**](PermissionApi.md#permissions_lookup_entity_stream) | **POST** /v1/tenants/{tenant_id}/permissions/lookup-entity-stream | lookup entity stream
[**permissions_lookup_subject**](PermissionApi.md#permissions_lookup_subject) | **POST** /v1/tenants/{tenant_id}/permissions/lookup-subject | lookup-subject
[**permissions_subject_permission**](PermissionApi.md#permissions_subject_permission) | **POST** /v1/tenants/{tenant_id}/permissions/subject-permission | subject permission


# **permissions_check**
> PermissionCheckResponse permissions_check(tenant_id, body)

check api

### Example


```python
import time
import os
import permify
from permify.models.check_body import CheckBody
from permify.models.permission_check_response import PermissionCheckResponse
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
    tenant_id = 'tenant_id_example' # str | Identifier of the tenant, if you are not using multi-tenancy (have only one tenant) use pre-inserted tenant <code>t1</code> for this field. Required, and must match the pattern \\“[a-zA-Z0-9-,]+\\“, max 64 bytes.
    body = permify.CheckBody() # CheckBody | 

    try:
        # check api
        api_response = api_instance.permissions_check(tenant_id, body)
        print("The response of PermissionApi->permissions_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionApi->permissions_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Identifier of the tenant, if you are not using multi-tenancy (have only one tenant) use pre-inserted tenant &lt;code&gt;t1&lt;/code&gt; for this field. Required, and must match the pattern \\“[a-zA-Z0-9-,]+\\“, max 64 bytes. | 
 **body** | [**CheckBody**](CheckBody.md)|  | 

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

expand api

### Example


```python
import time
import os
import permify
from permify.models.permission_expand_body import PermissionExpandBody
from permify.models.permission_expand_response import PermissionExpandResponse
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
    tenant_id = 'tenant_id_example' # str | Identifier of the tenant, if you are not using multi-tenancy (have only one tenant) use pre-inserted tenant <code>t1</code> for this field. Required, and must match the pattern \\“[a-zA-Z0-9-,]+\\“, max 64 bytes.
    body = permify.PermissionExpandBody() # PermissionExpandBody | 

    try:
        # expand api
        api_response = api_instance.permissions_expand(tenant_id, body)
        print("The response of PermissionApi->permissions_expand:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionApi->permissions_expand: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Identifier of the tenant, if you are not using multi-tenancy (have only one tenant) use pre-inserted tenant &lt;code&gt;t1&lt;/code&gt; for this field. Required, and must match the pattern \\“[a-zA-Z0-9-,]+\\“, max 64 bytes. | 
 **body** | [**PermissionExpandBody**](PermissionExpandBody.md)|  | 

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

lookup entity

### Example


```python
import time
import os
import permify
from permify.models.lookup_entity_body import LookupEntityBody
from permify.models.permission_lookup_entity_response import PermissionLookupEntityResponse
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
    tenant_id = 'tenant_id_example' # str | Identifier of the tenant, if you are not using multi-tenancy (have only one tenant) use pre-inserted tenant <code>t1</code> for this field. Required, and must match the pattern \\“[a-zA-Z0-9-,]+\\“, max 64 bytes.
    body = permify.LookupEntityBody() # LookupEntityBody | 

    try:
        # lookup entity
        api_response = api_instance.permissions_lookup_entity(tenant_id, body)
        print("The response of PermissionApi->permissions_lookup_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionApi->permissions_lookup_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Identifier of the tenant, if you are not using multi-tenancy (have only one tenant) use pre-inserted tenant &lt;code&gt;t1&lt;/code&gt; for this field. Required, and must match the pattern \\“[a-zA-Z0-9-,]+\\“, max 64 bytes. | 
 **body** | [**LookupEntityBody**](LookupEntityBody.md)|  | 

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

lookup entity stream

### Example


```python
import time
import os
import permify
from permify.models.lookup_entity_stream_body import LookupEntityStreamBody
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
    tenant_id = 'tenant_id_example' # str | Identifier of the tenant, if you are not using multi-tenancy (have only one tenant) use pre-inserted tenant <code>t1</code> for this field. Required, and must match the pattern \\“[a-zA-Z0-9-,]+\\“, max 64 bytes.
    body = permify.LookupEntityStreamBody() # LookupEntityStreamBody | 

    try:
        # lookup entity stream
        api_response = api_instance.permissions_lookup_entity_stream(tenant_id, body)
        print("The response of PermissionApi->permissions_lookup_entity_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionApi->permissions_lookup_entity_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Identifier of the tenant, if you are not using multi-tenancy (have only one tenant) use pre-inserted tenant &lt;code&gt;t1&lt;/code&gt; for this field. Required, and must match the pattern \\“[a-zA-Z0-9-,]+\\“, max 64 bytes. | 
 **body** | [**LookupEntityStreamBody**](LookupEntityStreamBody.md)|  | 

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

lookup-subject

### Example


```python
import time
import os
import permify
from permify.models.lookup_subject_body import LookupSubjectBody
from permify.models.permission_lookup_subject_response import PermissionLookupSubjectResponse
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
    tenant_id = 'tenant_id_example' # str | Identifier of the tenant, if you are not using multi-tenancy (have only one tenant) use pre-inserted tenant <code>t1</code> for this field. Required, and must match the pattern \\“[a-zA-Z0-9-,]+\\“, max 64 bytes.
    body = permify.LookupSubjectBody() # LookupSubjectBody | 

    try:
        # lookup-subject
        api_response = api_instance.permissions_lookup_subject(tenant_id, body)
        print("The response of PermissionApi->permissions_lookup_subject:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionApi->permissions_lookup_subject: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Identifier of the tenant, if you are not using multi-tenancy (have only one tenant) use pre-inserted tenant &lt;code&gt;t1&lt;/code&gt; for this field. Required, and must match the pattern \\“[a-zA-Z0-9-,]+\\“, max 64 bytes. | 
 **body** | [**LookupSubjectBody**](LookupSubjectBody.md)|  | 

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

subject permission

### Example


```python
import time
import os
import permify
from permify.models.permission_subject_permission_response import PermissionSubjectPermissionResponse
from permify.models.subject_permission_body import SubjectPermissionBody
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
    tenant_id = 'tenant_id_example' # str | Identifier of the tenant, if you are not using multi-tenancy (have only one tenant) use pre-inserted tenant <code>t1</code> for this field. Required, and must match the pattern \\“[a-zA-Z0-9-,]+\\“, max 64 bytes.
    body = permify.SubjectPermissionBody() # SubjectPermissionBody | 

    try:
        # subject permission
        api_response = api_instance.permissions_subject_permission(tenant_id, body)
        print("The response of PermissionApi->permissions_subject_permission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionApi->permissions_subject_permission: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Identifier of the tenant, if you are not using multi-tenancy (have only one tenant) use pre-inserted tenant &lt;code&gt;t1&lt;/code&gt; for this field. Required, and must match the pattern \\“[a-zA-Z0-9-,]+\\“, max 64 bytes. | 
 **body** | [**SubjectPermissionBody**](SubjectPermissionBody.md)|  | 

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

