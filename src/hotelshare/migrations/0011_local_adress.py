# Generated by Django 2.0.13 on 2019-03-21 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelshare', '0010_auto_20190321_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='local',
            name='adress',
            field=models.CharField(default='', max_length=300),
        ),
    ]