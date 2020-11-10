# Generated by Django 3.1.2 on 2020-11-07 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_driver_health_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='license_type',
            field=models.CharField(blank=True, choices=[('A', 'Class A'), ('B', 'Class B'), ('C', 'Class C'), ('D', 'Class D')], max_length=1, null=True),
        ),
    ]
