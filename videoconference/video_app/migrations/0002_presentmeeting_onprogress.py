# Generated by Django 5.0.3 on 2024-04-03 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='presentmeeting',
            name='onprogress',
            field=models.BooleanField(default=False),
        ),
    ]
