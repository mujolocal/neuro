# Generated by Django 2.2.1 on 2019-05-17 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moods', '0003_mood_streak'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mood',
            name='streak',
            field=models.SmallIntegerField(null=True),
        ),
    ]
