# Generated by Django 5.0.3 on 2024-04-14 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_app', '0007_alter_presentmeeting_participants'),
    ]

    operations = [
        migrations.AddField(
            model_name='presentmeeting',
            name='join_times',
            field=models.JSONField(default=dict),
        ),
    ]
