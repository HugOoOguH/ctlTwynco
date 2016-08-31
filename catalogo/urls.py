from django.conf.urls import url, include
from django.contrib import admin
from home import urls as UrlsHome
from django.conf import settings
from accounts import urls as UrlsAccounts
from publicity import urls as UrlsPublicity
from django.views.static import serve
from publicity.api import urls as apiUrls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(apiUrls)),
    url(r'^accounts/', include(UrlsAccounts,namespace="accounts")),
    url(r'^publicity/', include(UrlsPublicity,namespace="publicity")),
    url('', include('social.apps.django_app.urls', namespace="social")),
    url(
    	regex=r'^media/(?P<path>.*)$',
    	view=serve,
    	kwargs={'document_root':settings.MEDIA_ROOT}),
	url(r'^', include(UrlsHome)),
]
