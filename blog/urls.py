from django.conf.urls import url
from blog import views

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'), # /blog/
]

