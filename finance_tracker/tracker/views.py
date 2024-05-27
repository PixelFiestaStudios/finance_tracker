from django.shortcuts import render

from .plaid_integration import get_access_token, get_transactions

def index(request):
    # Placeholder for transactions
    transactions = []
    if request.method == 'POST':
        public_token = request.POST.get('public_token')
        access_token = get_access_token(public_token)
        transactions = get_transactions(access_token, '2023-01-01', '2023-12-31')
    return render(request, 'tracker/index.html', {'transactions': transactions})

