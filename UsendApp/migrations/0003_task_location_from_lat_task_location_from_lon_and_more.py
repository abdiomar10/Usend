# Generated by Django 5.0.7 on 2024-07-30 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UsendApp', '0002_task_proposed_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='location_from_lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='location_from_lon',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='location_to_lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='location_to_lon',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
