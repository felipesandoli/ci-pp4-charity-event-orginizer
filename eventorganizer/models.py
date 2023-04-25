from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone


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
    event_start = models.DateTimeField(default=timezone.now)
    event_end = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)
    archived = models.BooleanField(default=False)
    likes = models.ManyToManyField(
        User, blank=True, related_name='event_likes'
    )
    participants = models.ManyToManyField(
        User, blank=True, related_name='event_participants'
    )
    cover_image = CloudinaryField('image', default="default_image")

    class Meta:
        ordering = ['event_start']

    def __str__(self):
        return f"{self.name} by {self.owner}"

    def number_of_likes(self):
        return self.likes.count()

    def number_of_participants(self):
        return self.participants.count()
