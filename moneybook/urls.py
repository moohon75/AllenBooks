from django.conf.urls import url
from moneybook import views

urlpatterns = [
	url(r'^$', views.moneybook_list, name='moneybook_list'),
]
