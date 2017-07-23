from django.shortcuts import render
from django.utils import timezone
from .models import Transaction

def moneybook_list(request):
    transactions = Transaction.objects.filter().order_by('date')
    return render(request, 'moneybook/moneybook_list.html', {'transactions': transactions})