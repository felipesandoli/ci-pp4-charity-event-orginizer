from django import forms
from .models import Event


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
