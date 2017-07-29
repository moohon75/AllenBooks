from django.http import HttpResponse
from django.views.generic.base import TemplateView

#--- TemplateView
def hello(request):
	return HttpResponse("Hello Django!!")

class HomeView(TemplateView):

    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['object_list'] = ['polls', 'books', 'moneybook']
        return context
