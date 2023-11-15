"""
URL configuration for Whatsaf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from Whatsaf import settings
from django.conf.urls import handler400, handler403, handler404, handler500

urlpatterns = [
    path("WhatsafAdminByFounderCEO/", admin.site.urls),
    path("", include("WhatsafPortal.urls")),
    re_path(r'^RequiredImages/(?P<path>.*)$', serve, {'document_root' : settings.MEDIA_ROOT})
]

handler404 = "WhatsafPortal.views.error"
handler500 = "WhatsafPortal.views.error500"
handler403 = "WhatsafPortal.views.error"
handler400 = "WhatsafPortal.views.error"
admin.site.site_title = "Whatsaf"
admin.site.site_header = "Whatsaf"
admin.site.index_title = "Welcome to Whatsaf's Admin panel..."