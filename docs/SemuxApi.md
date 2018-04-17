# swagger_client.SemuxApi

All URIs are relative to *http://localhost/v2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_node**](SemuxApi.md#add_node) | **POST** /node | Add node
[**add_to_blacklist**](SemuxApi.md#add_to_blacklist) | **PUT** /blacklist | Add to blacklist
[**add_to_whitelist**](SemuxApi.md#add_to_whitelist) | **PUT** /whitelist | Add to whitelist
[**broadcast_raw_transaction**](SemuxApi.md#broadcast_raw_transaction) | **POST** /transaction/raw | Broadcast a raw transaction
[**compose_raw_transaction**](SemuxApi.md#compose_raw_transaction) | **GET** /compose-raw-transaction | Compose an unsigned raw transaction
[**create_account**](SemuxApi.md#create_account) | **POST** /account | Create account
[**get_account**](SemuxApi.md#get_account) | **GET** /account | Get account
[**get_account_transactions**](SemuxApi.md#get_account_transactions) | **GET** /account/transactions | Get account transactions
[**get_block_by_hash**](SemuxApi.md#get_block_by_hash) | **GET** /block-by-hash | Get block by hash
[**get_block_by_number**](SemuxApi.md#get_block_by_number) | **GET** /block-by-number | Get block by number
[**get_delegate**](SemuxApi.md#get_delegate) | **GET** /delegate | Get a delegate
[**get_delegates**](SemuxApi.md#get_delegates) | **GET** /delegates | Get all delegates
[**get_info**](SemuxApi.md#get_info) | **GET** /info | Get info
[**get_latest_block**](SemuxApi.md#get_latest_block) | **GET** /latest-block | Get latest block
[**get_latest_block_number**](SemuxApi.md#get_latest_block_number) | **GET** /latest-block-number | Get latest block number
[**get_peers**](SemuxApi.md#get_peers) | **GET** /peers | Get peers
[**get_pending_transactions**](SemuxApi.md#get_pending_transactions) | **GET** /pending-transactions | Get pending transactions
[**get_root**](SemuxApi.md#get_root) | **GET** / | Get root
[**get_transaction**](SemuxApi.md#get_transaction) | **GET** /transaction | Get transaction
[**get_transaction_limits**](SemuxApi.md#get_transaction_limits) | **GET** /transaction-limits | Get transaction limits
[**get_validators**](SemuxApi.md#get_validators) | **GET** /validators | Get validators
[**get_vote**](SemuxApi.md#get_vote) | **GET** /vote | Get vote
[**get_votes**](SemuxApi.md#get_votes) | **GET** /votes | Get votes
[**list_accounts**](SemuxApi.md#list_accounts) | **GET** /accounts | List accounts
[**register_delegate**](SemuxApi.md#register_delegate) | **POST** /transaction/delegate | Register delegate
[**sign_message**](SemuxApi.md#sign_message) | **GET** /sign-message | Sign a message
[**sign_raw_transaction**](SemuxApi.md#sign_raw_transaction) | **GET** /sign-raw-transaction | Sign an unsigned raw transaction
[**transfer**](SemuxApi.md#transfer) | **POST** /transaction/transfer | Transfer coins
[**unvote**](SemuxApi.md#unvote) | **POST** /transaction/unvote | Unvote
[**verify_message**](SemuxApi.md#verify_message) | **GET** /verify-message | Verify a message
[**vote**](SemuxApi.md#vote) | **POST** /transaction/vote | Vote


# **add_node**
> AddNodeResponse add_node(node)

Add node

Adds a node to node manager.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SemuxApi(swagger_client.ApiClient(configuration))
node = 'node_example' # str | Name of the node in host:port format

try:
    # Add node
    api_response = api_instance.add_node(node)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SemuxApi->add_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node** | **str**| Name of the node in host:port format | 

### Return type

[**AddNodeResponse**](AddNodeResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_to_blacklist**
> ApiHandlerResponse add_to_blacklist(ip)

Add to blacklist

Adds an IP address to blacklist.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SemuxApi(swagger_client.ApiClient(configuration))
ip = 'ip_example' # str | IP address

try:
    # Add to blacklist
    api_response = api_instance.add_to_blacklist(ip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SemuxApi->add_to_blacklist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**| IP address | 

### Return type

[**ApiHandlerResponse**](ApiHandlerResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_to_whitelist**
> ApiHandlerResponse add_to_whitelist(ip)

Add to whitelist

Adds an IP address to whitelist.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SemuxApi(swagger_client.ApiClient(configuration))
ip = 'ip_example' # str | IP address

try:
    # Add to whitelist
    api_response = api_instance.add_to_whitelist(ip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SemuxApi->add_to_whitelist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**| IP address | 

### Return type

[**ApiHandlerResponse**](ApiHandlerResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **broadcast_raw_transaction**
> SendTransactionResponse broadcast_raw_transaction(raw)

Broadcast a raw transaction

Broadcasts a raw transaction to the network.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SemuxApi(swagger_client.ApiClient(configuration))
raw = 'raw_example' # str | Raw transaction

try:
    # Broadcast a raw transaction
    api_response = api_instance.broadcast_raw_transaction(raw)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SemuxApi->broadcast_raw_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw** | **str**| Raw transaction | 

### Return type

[**SendTransactionResponse**](SendTransactionResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compose_raw_transaction**
> ComposeRawTransactionResponse compose_raw_transaction(network, type, fee, nonce, to=to, value=value, timestamp=timestamp, data=data)

Compose an unsigned raw transaction

Compose an unsigned raw transaction then return its hexadecimal encoded string. An unsigned raw transaction can be signed using /sign-raw-transaction API.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SemuxApi(swagger_client.ApiClient(configuration))
network = 'network_example' # str | Network name
type = 'type_example' # str | Transaction type
fee = 'fee_example' # str | Transaction fee in nano
nonce = 'nonce_example' # str | Transaction nonce
to = 'to_example' # str | Recipient's address (optional)
value = 'value_example' # str | Transaction value in nano (optional)
timestamp = 'timestamp_example' # str | Transaction timestamp in milliseconds. Default to current time. (optional)
data = 'data_example' # str | Hexadecimal encoded transaction data. (optional)

try:
    # Compose an unsigned raw transaction
    api_response = api_instance.compose_raw_transaction(network, type, fee, nonce, to=to, value=value, timestamp=timestamp, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SemuxApi->compose_raw_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**| Network name | 
 **type** | **str**| Transaction type | 
 **fee** | **str**| Transaction fee in nano | 
 **nonce** | **str**| Transaction nonce | 
 **to** | **str**| Recipient&#39;s address | [optional] 
 **value** | **str**| Transaction value in nano | [optional] 
 **timestamp** | **str**| Transaction timestamp in milliseconds. Default to current time. | [optional] 
 **data** | **str**| Hexadecimal encoded transaction data. | [optional] 

### Return type

[**ComposeRawTransactionResponse**](ComposeRawTransactionResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_account**
> CreateAccountResponse create_account(name=name)

Create account

Creates a new account.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SemuxApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | Assigned alias to the created account. (optional)

try:
    # Create account
    api_response = api_instance.create_account(name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SemuxApi->create_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Assigned alias to the created account. | [optional] 

### Return type

[**CreateAccountResponse**](CreateAccountResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account**
> GetAccountResponse get_account(address)

Get account

Returns an account.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SemuxApi(swagger_client.ApiClient(configuration))
address = 'address_example' # str | Address of account

try:
    # Get account
    api_response = api_instance.get_account(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SemuxApi->get_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Address of account | 

### Return type

[**GetAccountResponse**](GetAccountResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_transactions**
> GetAccountTransactionsResponse get_account_transactions(address, _from, to)

Get account transactions

Returns transactions from/to an account.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SemuxApi(swagger_client.ApiClient(configuration))
address = 'address_example' # str | Address of account
_from = '_from_example' # str | Starting range of transactions
to = 'to_example' # str | Ending range of transactions

try:
    # Get account transactions
    api_response = api_instance.get_account_transactions(address, _from, to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SemuxApi->get_account_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Address of account | 
 **_from** | **str**| Starting range of transactions | 
 **to** | **str**| Ending range of transactions | 

### Return type

[**GetAccountTransactionsResponse**](GetAccountTransactionsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_block_by_hash**
> GetBlockResponse get_block_by_hash(hash)

Get block by hash

Returns a block by block hash.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SemuxApi(swagger_client.ApiClient(configuration))
hash = 'hash_example' # str | Hash of block

try:
    # Get block by hash
    api_response = api_instance.get_block_by_hash(hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SemuxApi->get_block_by_hash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| Hash of block | 

### Return type

[**GetBlockResponse**](GetBlockResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_block_by_number**
> GetBlockResponse get_block_by_number(number)

Get block by number

Returns a block by block number.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SemuxApi(swagger_client.ApiClient(configuration))
number = 'number_example' # str | Number of block

try:
    # Get block by number
    api_response = api_instance.get_block_by_number(number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SemuxApi->get_block_by_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number** | **str**| Number of block | 

### Return type

[**GetBlockResponse**](GetBlockResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_delegate**
> GetDelegateResponse get_delegate(address)

Get a delegate

Returns a delegate.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SemuxApi(swagger_client.ApiClient(configuration))
address = 'address_example' # str | Delegate address

try:
    # Get a delegate
    api_response = api_instance.get_delegate(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SemuxApi->get_delegate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Delegate address | 

### Return type

[**GetDelegateResponse**](GetDelegateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_delegates**
> GetDelegatesResponse get_delegates()

Get all delegates

Returns a list of delegates.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SemuxApi(swagger_client.ApiClient(configuration))

try:
    # Get all delegates
    api_response = api_instance.get_delegates()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SemuxApi->get_delegates: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetDelegatesResponse**](GetDelegatesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_info**
> GetInfoResponse get_info()

Get info

Returns kernel info.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SemuxApi(swagger_client.ApiClient(configuration))

try:
    # Get info
    api_response = api_instance.get_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SemuxApi->get_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetInfoResponse**](GetInfoResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_block**
> GetLatestBlockResponse get_latest_block()

Get latest block

Returns the latest block.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SemuxApi(swagger_client.ApiClient(configuration))

try:
    # Get latest block
    api_response = api_instance.get_latest_block()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SemuxApi->get_latest_block: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetLatestBlockResponse**](GetLatestBlockResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_block_number**
> GetLatestBlockNumberResponse get_latest_block_number()

Get latest block number

Returns the number of the latest block.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SemuxApi(swagger_client.ApiClient(configuration))

try:
    # Get latest block number
    api_response = api_instance.get_latest_block_number()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SemuxApi->get_latest_block_number: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetLatestBlockNumberResponse**](GetLatestBlockNumberResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_peers**
> GetPeersResponse get_peers()

Get peers

Returns connected peers.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SemuxApi(swagger_client.ApiClient(configuration))

try:
    # Get peers
    api_response = api_instance.get_peers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SemuxApi->get_peers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetPeersResponse**](GetPeersResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pending_transactions**
> GetPendingTransactionsResponse get_pending_transactions()

Get pending transactions

Returns all the pending transactions.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SemuxApi(swagger_client.ApiClient(configuration))

try:
    # Get pending transactions
    api_response = api_instance.get_pending_transactions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SemuxApi->get_pending_transactions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetPendingTransactionsResponse**](GetPendingTransactionsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_root**
> GetRootResponse get_root()

Get root

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SemuxApi(swagger_client.ApiClient(configuration))

try:
    # Get root
    api_response = api_instance.get_root()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SemuxApi->get_root: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetRootResponse**](GetRootResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction**
> GetTransactionResponse get_transaction(hash)

Get transaction

Returns a transactions if exists.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SemuxApi(swagger_client.ApiClient(configuration))
hash = 'hash_example' # str | Transaction hash

try:
    # Get transaction
    api_response = api_instance.get_transaction(hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SemuxApi->get_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| Transaction hash | 

### Return type

[**GetTransactionResponse**](GetTransactionResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_limits**
> GetTransactionLimitsResponse get_transaction_limits(type)

Get transaction limits

Get minimum fee and maximum size.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SemuxApi(swagger_client.ApiClient(configuration))
type = 'type_example' # str | Type of transaction

try:
    # Get transaction limits
    api_response = api_instance.get_transaction_limits(type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SemuxApi->get_transaction_limits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Type of transaction | 

### Return type

[**GetTransactionLimitsResponse**](GetTransactionLimitsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_validators**
> GetValidatorsResponse get_validators()

Get validators

Returns a list of validators.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SemuxApi(swagger_client.ApiClient(configuration))

try:
    # Get validators
    api_response = api_instance.get_validators()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SemuxApi->get_validators: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetValidatorsResponse**](GetValidatorsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vote**
> GetVoteResponse get_vote(delegate, voter)

Get vote

Returns the vote from a voter to a delegate.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SemuxApi(swagger_client.ApiClient(configuration))
delegate = 'delegate_example' # str | Delegate address
voter = 'voter_example' # str | Voter address

try:
    # Get vote
    api_response = api_instance.get_vote(delegate, voter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SemuxApi->get_vote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegate** | **str**| Delegate address | 
 **voter** | **str**| Voter address | 

### Return type

[**GetVoteResponse**](GetVoteResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_votes**
> GetVotesResponse get_votes(delegate)

Get votes

Returns all the votes to a delegate

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SemuxApi(swagger_client.ApiClient(configuration))
delegate = 'delegate_example' # str | Delegate address

try:
    # Get votes
    api_response = api_instance.get_votes(delegate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SemuxApi->get_votes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegate** | **str**| Delegate address | 

### Return type

[**GetVotesResponse**](GetVotesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_accounts**
> ListAccountsResponse list_accounts()

List accounts

Returns accounts in the wallet.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SemuxApi(swagger_client.ApiClient(configuration))

try:
    # List accounts
    api_response = api_instance.list_accounts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SemuxApi->list_accounts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListAccountsResponse**](ListAccountsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_delegate**
> DoTransactionResponse register_delegate(_from, fee, data)

Register delegate

Registers as a delegate

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SemuxApi(swagger_client.ApiClient(configuration))
_from = '_from_example' # str | Registering address
fee = 'fee_example' # str | Transaction fee
data = 'data_example' # str | Delegate name

try:
    # Register delegate
    api_response = api_instance.register_delegate(_from, fee, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SemuxApi->register_delegate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **str**| Registering address | 
 **fee** | **str**| Transaction fee | 
 **data** | **str**| Delegate name | 

### Return type

[**DoTransactionResponse**](DoTransactionResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sign_message**
> SignMessageResponse sign_message(address, message)

Sign a message

Sign a message.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SemuxApi(swagger_client.ApiClient(configuration))
address = 'address_example' # str | Signing address
message = 'message_example' # str | Message to sign

try:
    # Sign a message
    api_response = api_instance.sign_message(address, message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SemuxApi->sign_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Signing address | 
 **message** | **str**| Message to sign | 

### Return type

[**SignMessageResponse**](SignMessageResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sign_raw_transaction**
> SignRawTransactionResponse sign_raw_transaction(raw, address)

Sign an unsigned raw transaction

Sign an unsigned raw transaction then return its hexadecimal encoded string. An unsigned raw transaction can be created using /compose-raw-transaction API.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SemuxApi(swagger_client.ApiClient(configuration))
raw = 'raw_example' # str | Unsigned raw transaction encoded in hexadecimal string.
address = 'address_example' # str | Signer's address. This address must exist in the wallet.

try:
    # Sign an unsigned raw transaction
    api_response = api_instance.sign_raw_transaction(raw, address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SemuxApi->sign_raw_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw** | **str**| Unsigned raw transaction encoded in hexadecimal string. | 
 **address** | **str**| Signer&#39;s address. This address must exist in the wallet. | 

### Return type

[**SignRawTransactionResponse**](SignRawTransactionResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer**
> DoTransactionResponse transfer(_from, to, value, fee, data)

Transfer coins

Transfers coins to another address.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SemuxApi(swagger_client.ApiClient(configuration))
_from = '_from_example' # str | Sending address
to = 'to_example' # str | Receiving address
value = 'value_example' # str | Amount of SEM to transfer
fee = 'fee_example' # str | Transaction fee
data = 'data_example' # str | Transaction data

try:
    # Transfer coins
    api_response = api_instance.transfer(_from, to, value, fee, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SemuxApi->transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **str**| Sending address | 
 **to** | **str**| Receiving address | 
 **value** | **str**| Amount of SEM to transfer | 
 **fee** | **str**| Transaction fee | 
 **data** | **str**| Transaction data | 

### Return type

[**DoTransactionResponse**](DoTransactionResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unvote**
> DoTransactionResponse unvote(_from, to, value, fee)

Unvote

Unvotes for a delegate.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SemuxApi(swagger_client.ApiClient(configuration))
_from = '_from_example' # str | Voting address
to = 'to_example' # str | Delegate address
value = 'value_example' # str | Vote amount
fee = 'fee_example' # str | Transaction fee

try:
    # Unvote
    api_response = api_instance.unvote(_from, to, value, fee)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SemuxApi->unvote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **str**| Voting address | 
 **to** | **str**| Delegate address | 
 **value** | **str**| Vote amount | 
 **fee** | **str**| Transaction fee | 

### Return type

[**DoTransactionResponse**](DoTransactionResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_message**
> VerifyMessageResponse verify_message(address, message, signature)

Verify a message

Verify a signed message.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SemuxApi(swagger_client.ApiClient(configuration))
address = 'address_example' # str | Address
message = 'message_example' # str | Message
signature = 'signature_example' # str | Signature to verify

try:
    # Verify a message
    api_response = api_instance.verify_message(address, message, signature)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SemuxApi->verify_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Address | 
 **message** | **str**| Message | 
 **signature** | **str**| Signature to verify | 

### Return type

[**VerifyMessageResponse**](VerifyMessageResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vote**
> DoTransactionResponse vote(_from, to, value, fee)

Vote

Votes for a delegate.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SemuxApi(swagger_client.ApiClient(configuration))
_from = '_from_example' # str | Voting address
to = 'to_example' # str | Delegate address
value = 'value_example' # str | Vote amount
fee = 'fee_example' # str | Transaction fee

try:
    # Vote
    api_response = api_instance.vote(_from, to, value, fee)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SemuxApi->vote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **str**| Voting address | 
 **to** | **str**| Delegate address | 
 **value** | **str**| Vote amount | 
 **fee** | **str**| Transaction fee | 

### Return type

[**DoTransactionResponse**](DoTransactionResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

