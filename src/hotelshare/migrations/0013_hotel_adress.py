# Generated by Django 2.0.13 on 2019-03-21 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotelshare', '0012_event_adress'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='adress',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='hotelshare.Local'),
        ),
    ]
