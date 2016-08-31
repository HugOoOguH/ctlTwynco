from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^marks/$', views.MarksListView.as_view(), name="mark_list"),
]