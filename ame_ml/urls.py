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

from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', MLHomeView.as_view(), name='ml_home'),
    url(r'^myfeeling/collect/$', CollectMyFeelingView.as_view(),
        name='collect_myfeeling'),
    url(r'^myfeeling/classification/$', ClassificationMyFeelingView.as_view(),
        name='classification_myfeeling'),
]

