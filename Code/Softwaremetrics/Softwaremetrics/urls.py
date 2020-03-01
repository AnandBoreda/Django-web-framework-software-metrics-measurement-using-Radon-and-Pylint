"""Softwaremetrics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
# from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Metrics.views import index, adminlogin, adminloginentered, logout, userlogin, userregister, viewuserdata, \
    activateuser, filedata, adminpage, userlogincheck1, uploadfile, viewfile, userpage, viewfildata, userfiledata

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$', index, name="index"),
    url(r'^index/', index, name="index"),
    url(r'^adminpage/', adminpage, name="adminpage"),
    url(r'^adminlogin/', adminlogin, name="adminlogin"),
    url(r'^adminloginentered/', adminloginentered, name="adminloginentered"),
    url(r'viewuserdata/', viewuserdata, name="viewuserdata"),
    url(r'activateuser/', activateuser, name="activateuser"),
    url(r'^filedata/', filedata, name="filedata"),
    url(r'^viewfile/', viewfile, name="viewfile"),
    url(r'^logout/', logout, name="logout"),
    url(r'^userlogincheck1/', userlogincheck1, name="userlogincheck1"),
    url(r'^userlogin/', userlogin, name="userlogin"),
    url(r'^userpage/', userpage, name="userpage"),
    url(r'^userregister/', userregister, name="userregister"),
    url(r'^uploadfile/', uploadfile, name="uploadfile"),
    url(r'^viewfildata/', viewfildata, name="viewfildata"),
    url(r'^userfiledata/', userfiledata, name="userfiledata"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)