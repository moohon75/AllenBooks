from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView
from django.utils import timezone
from blog.models import Post

#--- Class-based GenericView
class IndexView(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'blog_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Post.objects.order_by('created_date').reverse()[:5]