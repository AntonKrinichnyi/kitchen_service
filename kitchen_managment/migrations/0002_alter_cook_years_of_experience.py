# Generated by Django 4.2.18 on 2025-01-21 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen_managment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cook',
            name='years_of_experience',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
