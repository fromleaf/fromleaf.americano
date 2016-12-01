from django.shortcuts import render
from django.views.generic import TemplateView


class PlayHomeView(TemplateView):
    template_name = 'ame_play/play.html'
