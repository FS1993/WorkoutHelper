# Generated by Django 2.1.1 on 2018-10-03 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0002_auto_20181003_0759'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='level',
            name='level_id',
            field=models.IntegerField(default=1),
        ),
    ]