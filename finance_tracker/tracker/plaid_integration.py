import plaid
from django.conf import settings

client = plaid.Client(client_id=settings.PLAID_CLIENT_ID,
                      secret=settings.PLAID_SECRET,
                      environment=settings.PLAID_ENVIRONMENT)

def get_access_token(public_token):
    response = client.Item.public_token.exchange(public_token)
    return response['access_token']

def get_transactions(access_token, start_date, end_date):
    response = client.Transactions.get(access_token, start_date, end_date)
    return response['transactions']
