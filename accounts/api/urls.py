from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns=[
	url(r'^profile/$', views.ProfileList.as_view(), name="profile_list"),
	url(r'^profile/(?P<pk>[0-9]+)/$', views.ProfileDetail.as_view(), name="profile_detail"),
	url(r'^user/$', views.UserList.as_view(), name="user_list"),
	url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name="user_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)