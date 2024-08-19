# Generated by Django 5.0.7 on 2024-07-30 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UsendApp', '0006_profile_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(blank=True, choices=[('client', 'Client'), ('runner', 'Runner')], max_length=10, null=True),
        ),
    ]
