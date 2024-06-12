# tracker/views.py

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import plaid
from plaid.api import plaid_api
from plaid.model.products import Products
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from plaid.model.link_token_create_request_user import LinkTokenCreateRequestUser
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.country_code import CountryCode
from plaid.exceptions import ApiException
from django.conf import settings
import json
import logging

# Set up logging
logger = logging.getLogger(__name__)

configuration = plaid.Configuration(
    host=plaid.Environment.Sandbox,
    api_key={
        'clientId': settings.PLAID_CLIENT_ID,
        'secret': settings.PLAID_SECRET
    }
)

api_client = plaid.ApiClient(configuration)
client = plaid_api.PlaidApi(api_client)

def index(request):
    return render(request, 'tracker/index.html')

@csrf_exempt
def create_link_token(request):
    try:
        request_data = LinkTokenCreateRequest(
            products=[Products('auth'), Products('transactions')],
            client_name="Your App Name",
            country_codes=[CountryCode('US')],
            language='en',
            user=LinkTokenCreateRequestUser(client_user_id='unique_user_id'),
            redirect_uri='http://localhost:8000/exchange_public_token'
        )
        response = client.link_token_create(request_data)
        logger.info(f"Plaid Link Token Response: {response}")
        return JsonResponse(response.to_dict())
    except ApiException as e:
        logger.error(f"Plaid API Exception: {e.body}")
        return JsonResponse({'error': json.loads(e.body)}, status=e.status)

@csrf_exempt
def exchange_public_token(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        public_token = data.get('public_token')
        try:
            request_data = ItemPublicTokenExchangeRequest(public_token=public_token)
            response = client.item_public_token_exchange(request_data)
            access_token = response['access_token']
            item_id = response['item_id']
            return JsonResponse({'access_token': access_token, 'item_id': item_id})
        except ApiException as e:
            logger.error(f"Plaid API Exception: {e.body}")
            return JsonResponse({'error': json.loads(e.body)}, status=e.status)
    return JsonResponse({'error': 'Invalid request method'}, status=400)
