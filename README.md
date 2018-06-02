# swagger-client
Semux is an experimental high-performance blockchain platform that powers decentralized application.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.1.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen
For more information, please visit [https://www.semux.org](https://www.semux.org)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/mdodong/semuxapi-py.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/mdodong/semuxapi-py.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'
swagger_client.configuration.host = 'YOUR_HOST'
# create an instance of the API class
api_instance = swagger_client.SemuxApi()
node = 'node_example' # str | Address of the node in host:port format

try:
    # Add node
    api_response = api_instance.add_node(node)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SemuxApi->add_node: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost/v2.1.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*SemuxApi* | [**add_node**](docs/SemuxApi.md#add_node) | **POST** /node | Add node
*SemuxApi* | [**add_to_blacklist**](docs/SemuxApi.md#add_to_blacklist) | **PUT** /blacklist | Add to blacklist
*SemuxApi* | [**add_to_whitelist**](docs/SemuxApi.md#add_to_whitelist) | **PUT** /whitelist | Add to whitelist
*SemuxApi* | [**broadcast_raw_transaction**](docs/SemuxApi.md#broadcast_raw_transaction) | **POST** /transaction/raw | Broadcast a raw transaction
*SemuxApi* | [**compose_raw_transaction**](docs/SemuxApi.md#compose_raw_transaction) | **GET** /compose-raw-transaction | Compose an unsigned raw transaction
*SemuxApi* | [**create_account**](docs/SemuxApi.md#create_account) | **POST** /account | Create or import an account
*SemuxApi* | [**delete_account**](docs/SemuxApi.md#delete_account) | **DELETE** /account | Delete account
*SemuxApi* | [**get_account**](docs/SemuxApi.md#get_account) | **GET** /account | Get account
*SemuxApi* | [**get_account_pending_transactions**](docs/SemuxApi.md#get_account_pending_transactions) | **GET** /account/pending-transactions | Get pending transactions of the account
*SemuxApi* | [**get_account_transactions**](docs/SemuxApi.md#get_account_transactions) | **GET** /account/transactions | Get account transactions
*SemuxApi* | [**get_account_votes**](docs/SemuxApi.md#get_account_votes) | **GET** /account/votes | Get account votes
*SemuxApi* | [**get_block_by_hash**](docs/SemuxApi.md#get_block_by_hash) | **GET** /block-by-hash | Get block by hash
*SemuxApi* | [**get_block_by_number**](docs/SemuxApi.md#get_block_by_number) | **GET** /block-by-number | Get block by number
*SemuxApi* | [**get_delegate**](docs/SemuxApi.md#get_delegate) | **GET** /delegate | Get a delegate
*SemuxApi* | [**get_delegates**](docs/SemuxApi.md#get_delegates) | **GET** /delegates | Get all delegates
*SemuxApi* | [**get_info**](docs/SemuxApi.md#get_info) | **GET** /info | Get info
*SemuxApi* | [**get_latest_block**](docs/SemuxApi.md#get_latest_block) | **GET** /latest-block | Get latest block
*SemuxApi* | [**get_latest_block_number**](docs/SemuxApi.md#get_latest_block_number) | **GET** /latest-block-number | Get latest block number
*SemuxApi* | [**get_peers**](docs/SemuxApi.md#get_peers) | **GET** /peers | Get peers
*SemuxApi* | [**get_pending_transactions**](docs/SemuxApi.md#get_pending_transactions) | **GET** /pending-transactions | Get pending transactions
*SemuxApi* | [**get_root**](docs/SemuxApi.md#get_root) | **GET** / | Get root
*SemuxApi* | [**get_syncing_progress**](docs/SemuxApi.md#get_syncing_progress) | **GET** /syncing | Get syncing progress
*SemuxApi* | [**get_transaction**](docs/SemuxApi.md#get_transaction) | **GET** /transaction | Get transaction
*SemuxApi* | [**get_transaction_limits**](docs/SemuxApi.md#get_transaction_limits) | **GET** /transaction-limits | Get transaction limits
*SemuxApi* | [**get_validators**](docs/SemuxApi.md#get_validators) | **GET** /validators | Get validators
*SemuxApi* | [**get_vote**](docs/SemuxApi.md#get_vote) | **GET** /vote | Get vote
*SemuxApi* | [**get_votes**](docs/SemuxApi.md#get_votes) | **GET** /votes | Get a delegate&#39;s votes
*SemuxApi* | [**list_accounts**](docs/SemuxApi.md#list_accounts) | **GET** /accounts | List accounts
*SemuxApi* | [**register_delegate**](docs/SemuxApi.md#register_delegate) | **POST** /transaction/delegate | Register delegate
*SemuxApi* | [**sign_message**](docs/SemuxApi.md#sign_message) | **GET** /sign-message | Sign a message
*SemuxApi* | [**sign_raw_transaction**](docs/SemuxApi.md#sign_raw_transaction) | **GET** /sign-raw-transaction | Sign an unsigned raw transaction
*SemuxApi* | [**transfer**](docs/SemuxApi.md#transfer) | **POST** /transaction/transfer | Transfer coins
*SemuxApi* | [**unvote**](docs/SemuxApi.md#unvote) | **POST** /transaction/unvote | Unvote
*SemuxApi* | [**verify_message**](docs/SemuxApi.md#verify_message) | **GET** /verify-message | Verify a message
*SemuxApi* | [**vote**](docs/SemuxApi.md#vote) | **POST** /transaction/vote | Vote


## Documentation For Models

 - [AccountType](docs/AccountType.md)
 - [AccountVoteType](docs/AccountVoteType.md)
 - [ApiHandlerResponse](docs/ApiHandlerResponse.md)
 - [BlockType](docs/BlockType.md)
 - [DelegateType](docs/DelegateType.md)
 - [InfoType](docs/InfoType.md)
 - [PeerType](docs/PeerType.md)
 - [PendingTransactionType](docs/PendingTransactionType.md)
 - [SyncingProgressType](docs/SyncingProgressType.md)
 - [TransactionLimitsType](docs/TransactionLimitsType.md)
 - [TransactionType](docs/TransactionType.md)
 - [AddNodeResponse](docs/AddNodeResponse.md)
 - [ComposeRawTransactionResponse](docs/ComposeRawTransactionResponse.md)
 - [CreateAccountResponse](docs/CreateAccountResponse.md)
 - [DeleteAccountResponse](docs/DeleteAccountResponse.md)
 - [DoTransactionResponse](docs/DoTransactionResponse.md)
 - [GetAccountPendingTransactionsResponse](docs/GetAccountPendingTransactionsResponse.md)
 - [GetAccountResponse](docs/GetAccountResponse.md)
 - [GetAccountTransactionsResponse](docs/GetAccountTransactionsResponse.md)
 - [GetAccountVotesResponse](docs/GetAccountVotesResponse.md)
 - [GetBlockResponse](docs/GetBlockResponse.md)
 - [GetDelegateResponse](docs/GetDelegateResponse.md)
 - [GetDelegatesResponse](docs/GetDelegatesResponse.md)
 - [GetInfoResponse](docs/GetInfoResponse.md)
 - [GetLatestBlockNumberResponse](docs/GetLatestBlockNumberResponse.md)
 - [GetLatestBlockResponse](docs/GetLatestBlockResponse.md)
 - [GetPeersResponse](docs/GetPeersResponse.md)
 - [GetPendingTransactionsResponse](docs/GetPendingTransactionsResponse.md)
 - [GetRootResponse](docs/GetRootResponse.md)
 - [GetSyncingProgressResponse](docs/GetSyncingProgressResponse.md)
 - [GetTransactionLimitsResponse](docs/GetTransactionLimitsResponse.md)
 - [GetTransactionResponse](docs/GetTransactionResponse.md)
 - [GetValidatorsResponse](docs/GetValidatorsResponse.md)
 - [GetVoteResponse](docs/GetVoteResponse.md)
 - [GetVotesResponse](docs/GetVotesResponse.md)
 - [ListAccountsResponse](docs/ListAccountsResponse.md)
 - [SignMessageResponse](docs/SignMessageResponse.md)
 - [SignRawTransactionResponse](docs/SignRawTransactionResponse.md)
 - [VerifyMessageResponse](docs/VerifyMessageResponse.md)


## Documentation For Authorization


## basicAuth

- **Type**: HTTP basic authentication


## Author



