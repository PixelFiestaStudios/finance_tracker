from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from plaid.model import link_token_create_request, link_token_create_request_user, country_code, products, item_public_token_exchange_request

def index(request):
    return render(request, 'index.html')

def create_link_token(request):
    try:
        request_data = link_token_create_request.LinkTokenCreateRequest(
            products=[products.Products("transactions")],
            client_name="Plaid Test App",
            country_codes=[country_code.CountryCode('US')],
            language='en',
            user=link_token_create_request_user.LinkTokenCreateRequestUser(client_user_id=str(request.user.id)),
        )
        response = settings.PLAID_CLIENT.link_token_create(request_data)
        return JsonResponse(response.to_dict())
    except Exception as e:
        return JsonResponse({"error": str(e)})

def exchange_public_token(request):
    public_token = request.POST.get('public_token')
    try:
        request_data = item_public_token_exchange_request.ItemPublicTokenExchangeRequest(
            public_token=public_token
        )
        response = settings.PLAID_CLIENT.item_public_token_exchange(request_data)
        return JsonResponse(response.to_dict())
    except Exception as e:
        return JsonResponse({"error": str(e)})
