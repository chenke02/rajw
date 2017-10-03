"""Django1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from learn import views as learn_views
from django.conf import settings

urlpatterns = [
    url(r'^$', learn_views.index1_1, name='index1_1'),
    url(r'^index1_1_1/(\d+)/(\d+)/$', learn_views.index1_1_1, name='index1_1_1'),
    url(r'^index5_1/(\d+)/$', learn_views.index5_1, name='index5_1'),
    url(r'^index5_2/(\d+)/$', learn_views.index5_2, name='index5_2'),
    url(r'^index5_6/$', learn_views.index5_6, name='index5_6'),
    url(r'^admin/', admin.site.urls),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

]