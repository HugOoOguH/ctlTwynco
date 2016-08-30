from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^publicity', views.PublicityListView.as_view(), name="publicity"),
]