# -*- coding: utf-8 -*-

import simplejson as json

from django.views.generic import TemplateView
from django.conf import settings

from ame_common import utils
from .models import *


class HomeView(TemplateView):
    template_name = "ame_home/home.html"

    def set_about_context(self, context):
        path = settings.BASE_DIR + '/static/my_data/'

        mydata_file = utils.read_file_from_local(path, 'mydata.json')
        result_json = json.load(mydata_file)

        context['about'] = result_json['about']
        context['skill'] = result_json['skill']

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        self.set_about_context(context)

        return context
