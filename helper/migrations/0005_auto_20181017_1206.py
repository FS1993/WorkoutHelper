# Generated by Django 2.1.1 on 2018-10-17 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0004_exercise_reps'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='bar',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='parallel_bars',
            field=models.BooleanField(default='False'),
        ),
    ]
