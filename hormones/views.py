from django.shortcuts import render
from django.views.generic import TemplateView
from hormones.models import Hormone, Record, RecordValue


class BaseView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        
        context['hormones'] = Hormone.objects.all()
        return context
