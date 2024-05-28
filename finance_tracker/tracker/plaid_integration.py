# tracker/plaid_integration.py

import plaid
from plaid.api import plaid_api
from plaid.model.transactions_get_request import TransactionsGetRequest
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.accounts_get_request import AccountsGetRequest
from django.conf import settings
from plaid import Configuration, ApiClient

configuration = Configuration(
    host=plaid.Environment.Sandbox if settings.PLAID_ENVIRONMENT == 'sandbox' else plaid.Environment.Development,  # Change to the appropriate environment
    api_key={
        'clientId': settings.PLAID_CLIENT_ID,
        'secret': settings.PLAID_SECRET,
    }
)
api_client = ApiClient(configuration)
client = plaid_api.PlaidApi(api_client)

def get_access_token(public_token):
    request = ItemPublicTokenExchangeRequest(
        public_token=public_token
    )
    response = client.item_public_token_exchange(request)
    return response['access_token']

def get_accounts(access_token):
    request = AccountsGetRequest(access_token=access_token)
    response = client.accounts_get(request)
    return response['accounts']

def get_transactions(access_token, start_date, end_date):
    request = TransactionsGetRequest(
        access_token=access_token,
        start_date=start_date,
        end_date=end_date,
        options={}
    )
    response = client.transactions_get(request)
    return response['transactions']
