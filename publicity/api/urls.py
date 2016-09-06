from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns=[
	url(r'^marks/$', views.MarkList.as_view(), name="mark_list"),
	url(r'^marks/(?P<pk>[0-9]+)/$', views.MarkDetail.as_view(), name="mark_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)