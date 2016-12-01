# -*- coding: utf-8 -*-

"""americano URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from ame_home import urls as home_urls
from ame_play import urls as play_urls
from ame_ml import urls as ml_urls

urlpatterns = [
    # my portfolio urls
    url(r'^', include(home_urls)),

    # my playground urls
    url(r'^play/', include(play_urls)),

    # practise ml
    url(r'^ml/', include(ml_urls)),

    # admin url
    url(r'^admin/', admin.site.urls),
]
