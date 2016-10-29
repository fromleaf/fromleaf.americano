# -*- coding: utf-8 -*-

from django.views.generic import TemplateView

from .models import *

class HomeMainView(TemplateView):
    template_name = "ame_home/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeMainView, self).get_context_data(**kwargs)

        about = About.objects.get(id=1)
        programming_skills = Skill.objects.filter(
            skill_set__title='programming').prefetch_related('skill_set')
        coworking_skills = Skill.objects.filter(
            skill_set__title='coworking').prefetch_related('skill_set')

        context['about'] = about
        context['programming_skills'] = programming_skills
        context['coworking_skills'] = coworking_skills

        return context

