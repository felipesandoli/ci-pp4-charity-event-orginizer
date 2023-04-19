# Generated by Django 3.2.18 on 2023-04-19 22:04

from django.db import migrations, models
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('eventorganizer', '0002_auto_20230419_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='address',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='city',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='country',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=location_field.models.plain.PlainLocationField(default='', max_length=63),
            preserve_default=False,
        ),
    ]