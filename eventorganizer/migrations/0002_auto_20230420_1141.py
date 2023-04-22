# Generated by Django 3.2.18 on 2023-04-20 10:41

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eventorganizer', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['event_start']},
        ),
        migrations.AddField(
            model_name='event',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='cover_image',
            field=cloudinary.models.CloudinaryField(default='default_image', max_length=255, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='event',
            name='event_end',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='event',
            name='event_start',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='event',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='event_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='event_participants', to=settings.AUTH_USER_MODEL),
        ),
    ]