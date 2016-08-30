from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.HomeList.as_view(), name="home"),
]