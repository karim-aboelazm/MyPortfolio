from django.contrib import admin
from django.conf.urls import handler404, handler500
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.utils.translation import gettext_lazy as _

import django

def custom_page_not_found(request):
    return django.views.defaults.page_not_found(request, None)

def custom_server_error(request):
    return django.views.defaults.server_error(request)

urlpatterns = [
    path("", include("portfolio.urls", namespace="porto")),
    path("admin/", admin.site.urls),
    path('i18n/',include('django.conf.urls.i18n')),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path("404/", custom_page_not_found),
    path("500/", custom_server_error),
]

if settings.DEBUG or not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

