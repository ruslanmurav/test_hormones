import os

from django.http import FileResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from matplotlib.dates import DateFormatter

from test_hormones import settings
from .models import Hormone, Record, RecordValue
from .forms import HormoneValueForm, RecordForm
from qsstats import QuerySetStats
import matplotlib.pyplot as plt


class BaseView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        photo_names = []
        context = super().get_context_data(**kwargs)
        context['hormones'] = Hormone.objects.all()
        context['hormone_value_form'] = HormoneValueForm(hormones=context['hormones'])
        context['record_form'] = RecordForm()
        all_hormones = Hormone.objects.all()

        for hormone in all_hormones:
            hormone_records = RecordValue.objects.filter(hormone_id=hormone.id)

            x = []
            y = []

            for rec in hormone_records:
                record = Record.objects.get(id=rec.record_id)

                # print(record)
                #
                # print(record.record_date.day)

                x.append(record.record_date.day)
                y.append(rec.value)

            plt.plot(x, y)
            plt.xlabel('Дата')
            plt.ylabel('Значение гормона')
            plt.title(f'{hormone.hormone_name}')

            plt.gca().xaxis.set_major_formatter(DateFormatter('%d-%m'))
            plt.gcf().autofmt_xdate()

            plt.savefig(os.path.join(settings.BASE_DIR, f'static/vendor/img/{hormone.hormone_name}.jpg'), format='jpeg')
            photo_names.append(f'vendor/img/{hormone.hormone_name}.jpg')

            plt.close()

        context['photo_names'] = photo_names

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


class ImageServeView(View):
    def get(self, request, filename):
        file_path = os.path.join(settings.BASE_DIR, filename)
        with open(file_path, 'rb') as file:
            response = FileResponse(file)
            return response
