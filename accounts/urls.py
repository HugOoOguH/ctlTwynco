from django.conf.urls import url
from django.contrib.auth.views import logout, login, logout_then_login
from . import views

urlpatterns = [
	url(r'^registry/$', views.RegistryView.as_view(), name="registry"),
	url(r'^profile/$', views.ProfileView.as_view(), name="profile"),
	url(r'^login/$', login, name="login"),
	url(r'^logout/$', logout, name="logout"),
	url(r'^logout_then_login/$', logout_then_login, name="logout_then_login"),
]