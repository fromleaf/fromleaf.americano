# -*- coding: utf-8 -*-

import simplejson as json

from django.views.generic import TemplateView
from django.conf import settings

from ame_common import utils
from .models import *


class HomeView(TemplateView):
    template_name = "ame_home/home.html"
    my_data_path = settings.BASE_DIR + '/static/my_data/'

    def set_aboutme_context(self, context, json_data):
        result_json = json.load(json_data)

        context['about'] = result_json['about']
        context['skill'] = result_json['skill']

    def set_experience_context(self, context, json_data):
        result_json = json.load(json_data)

        context['companies'] = result_json['companies']

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        if settings.ENG_VERSION:
            my_info = utils.read_file_from_local(self.my_data_path,
                                                 'eng_my_info.json')
            my_experience = utils.read_file_from_local(self.my_data_path,
                                                       'eng_my_experience.json')
        else:
            my_info = utils.read_file_from_local(self.my_data_path,
                                                 'kor_my_info.json')

        self.set_aboutme_context(context, my_info)
        self.set_experience_context(context, my_experience)

        return context
