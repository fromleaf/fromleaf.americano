from django.shortcuts import render
from django.views.generic import TemplateView, FormView

from .forms import CollectMyFeelingForm
from .models import MyFeeling

class MLHomeView(TemplateView):
    template_name = 'ame_ml/main.html'


class CollectMyFeelingView(FormView):
    template_name = 'ame_ml/collect_myfeeling.html'
    form_class = CollectMyFeelingForm

    success_url = '/thanks/'

    @staticmethod
    def get_myfeelings():
        myfeelings = MyFeeling.objects.all()
        return myfeelings

    def get_context_data(self, **kwargs):
        context = super(CollectMyFeelingView, self).get_context_data(**kwargs)

        context['myfeelings'] = CollectMyFeelingView.get_myfeelings()
        context['form'] = self.form_class

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()

        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()

        return render(request, self.template_name, context)

    def form_valid(self, form):

        return super(CollectMyFeelingView, self).form_valid(form)


class ClassificationMyFeelingView(TemplateView):
    template_name = 'ame_ml/classification_myfeeling.html'
