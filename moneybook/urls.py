from django.conf.urls import url
from moneybook import views

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'), # /moneybook/
]
