from django import forms
from .models import Event


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'name',
            'type',
            'category',
            'summary',
            'description',
            'address',
            'city',
            'country',
            'start_date',
            'start_time',
            'end_date',
            'end_time',
            'cover_image'
        ]
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput(),
            'start_time': TimeInput(format='%H:%M'),
            'end_time': TimeInput(format='%H:%M'),
        }
