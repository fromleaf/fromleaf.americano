# -*- coding: utf-8 -*-

from django.views.generic import TemplateView

class HomeMainView(TemplateView):
        template_name = "ame_home/home.html"

class HomeMainView_2(TemplateView):
    template_name = "ame_home/home_2.html"

