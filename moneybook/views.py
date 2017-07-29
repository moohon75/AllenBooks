from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView
from django.utils import timezone
from .models import Transaction

#--- Class-based GenericView
class IndexView(ListView):
    template_name = 'moneybook/index.html'
    context_object_name = 'moneybook_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Transaction.objects.order_by('name')[:5]

	