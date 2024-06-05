# Generated by Django 5.0.3 on 2024-04-04 03:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_app', '0003_presentmeeting_participants'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='presentmeeting',
            name='allowed_participants',
            field=models.ManyToManyField(related_name='allowed_in_meetings', to=settings.AUTH_USER_MODEL),
        ),
    ]
