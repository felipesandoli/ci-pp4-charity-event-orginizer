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
            'event_start',
            'event_end',
            'cover_image'
        ]
