from datetime import datetime
from django import forms
from .models import Hormone, Record


class HormoneValueForm(forms.Form):
    def __init__(self, hormones, *args, **kwargs):
        super(HormoneValueForm, self).__init__(*args, **kwargs)
        for hormone in hormones:
            self.fields[str(hormone.id)] = forms.IntegerField(
                widget=forms.TextInput(attrs={
                    'type': 'range',
                    'min': '1',
                    'max': '100',
                    'oninput': f'updateOutput(this, {hormone.id})',  # Передаем ID гормона
                })
            )
        

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = []

    def save(self, force_insert=False, force_update=False, commit=True):
        current_date = datetime.today()
        date_string = current_date.strftime("%Y-%m-%d")
        
        flag = False
        records = Record.objects.all()
        for record in records:
            record_date_format = record.record_date.strftime("%Y-%m-%d")
            if date_string in record_date_format:
                print('Вы сегодня уже вводили ощущаемые значения гормонов')
                raise ValueError('Запись уже создана')

        return super(RecordForm, self).save()

# Остальной код из forms.py, если есть
