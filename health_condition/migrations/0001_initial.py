# Generated by Django 3.1.2 on 2020-11-16 19:19

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0008_auto_20201116_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthCondition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heart_rate', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(200)])),
                ('body_temperature', models.IntegerField(validators=[django.core.validators.MinValueValidator(34), django.core.validators.MaxValueValidator(40)])),
                ('respiration_rate_per_minute', models.IntegerField(validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(25)])),
                ('blood_pressure_systolic', models.IntegerField(validators=[django.core.validators.MinValueValidator(100), django.core.validators.MaxValueValidator(200)])),
                ('blood_pressure_diastolic', models.IntegerField(validators=[django.core.validators.MinValueValidator(80), django.core.validators.MaxValueValidator(140)])),
                ('blood_oxygen_level', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('blood_alcohol_content', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('drugs_alcohol_content', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='driver_condition', to='users.driver')),
            ],
        ),
    ]
