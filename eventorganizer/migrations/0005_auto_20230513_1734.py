# Generated by Django 3.2.18 on 2023-05-13 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventorganizer', '0004_auto_20230513_1704'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['start_date']},
        ),
        migrations.RemoveField(
            model_name='event',
            name='event_end',
        ),
        migrations.RemoveField(
            model_name='event',
            name='event_start',
        ),
    ]
