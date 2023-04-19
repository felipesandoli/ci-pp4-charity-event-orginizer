from django.db import models
from django.contrib.auth.models import User
from location_field.models.plain import PlainLocationField


class Event(models.Model):
    # Event type and category choices
    EVENT_TYPE_CHOICES = (
        ('VOLUNTEERING', 'Volunteering'),
        ('FUNCRAISING', 'Fundraising'),
    )
    CATEGORY_CHOICES = (
        ('ANIMAL WELFARE', 'Animal Welfare'),
        ('EDUCATIONAL', 'Educational'),
        ('ENVIRONMENTAL', 'Environmental'),
        ('HEALTCARE', 'Healthcare'),
        ('HUMANRIGHTS', 'Human Rights'),
    )

    name = models.CharField(max_length=100)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='owened_event'
    )
    type = models.CharField(max_length=20, choices=EVENT_TYPE_CHOICES)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    summary = models.TextField(help_text='Enter a short summary of your event')
    description = models.TextField(
        help_text='Enter a full description of your event'
    )
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    location = PlainLocationField(based_fields=['address', 'city', 'country'])

    def __str__(self):
        return f"{self.name} by {self.owner}"
