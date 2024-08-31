# Generated by Django 5.0.4 on 2024-04-18 11:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0013_alter_location_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='rooms.city'),
        ),
    ]
