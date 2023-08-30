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

# Остальной код из forms.py, если есть
