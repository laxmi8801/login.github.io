# Generated by Django 3.2.7 on 2021-12-15 10:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0008_alter_data_pincode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='max',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(2)]),
        ),
        migrations.AlterField(
            model_name='data',
            name='min',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
