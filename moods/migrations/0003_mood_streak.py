# Generated by Django 2.2.1 on 2019-05-17 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moods', '0002_mood_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='mood',
            name='streak',
            field=models.SmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
