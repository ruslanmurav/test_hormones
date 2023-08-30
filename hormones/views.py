from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Hormone, Record, RecordValue
from .forms import HormoneValueForm, RecordForm


class BaseView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hormones'] = Hormone.objects.all()
        context['hormone_value_form'] = HormoneValueForm(hormones=context['hormones'])
        context['record_form'] = RecordForm()
        return context

    def post(self, request, *args, **kwargs):
        record_form = RecordForm(request.POST)
        hormone_value_form = HormoneValueForm(Hormone.objects.all(), request.POST)

        if record_form.is_valid() and hormone_value_form.is_valid():
            record = record_form.save()
            hormone_values = []

            for hormone in hormone_value_form.cleaned_data:
                value = hormone_value_form.cleaned_data[hormone]
                hormone_values.append(RecordValue(hormone_id=hormone, record=record, value=value))

            RecordValue.objects.bulk_create(hormone_values)

        context = self.get_context_data()
        context['hormone_value_form'] = hormone_value_form
        context['record_form'] = record_form
        return self.render_to_response(context)
