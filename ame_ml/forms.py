# -*- coding: utf-8 -*-

from django.forms import ModelForm, ChoiceField, SelectDateWidget
from django.contrib.admin import widgets
from django.utils.translation import ugettext_lazy as _

from .models import MyFeeling


GRADE_CHOICES = (
        ('WORST', 'Worst'),
        ('BAD', 'Bad'),
        ('NORMAL', 'Normal'),
        ('GOOD', 'Good'),
        ('BEST', 'Best'),
    )


class CollectMyFeelingForm(ModelForm):

    grade = ChoiceField(choices=GRADE_CHOICES)

    class Meta:
        model = MyFeeling
        fields = [
            'created_date',
            'morning', 'afternoon', 'evening',
            'after_breakfast', 'after_lunch', 'after_dinner',
            'grade'
        ]
        widgets = {
            'created_date': SelectDateWidget(),
        }
        labels = {
            'created_date': _('Date'),
        }
        help_texts = {
            'created_date': _('Select Today'),
        }