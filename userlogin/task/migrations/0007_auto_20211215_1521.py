# Generated by Django 3.2.7 on 2021-12-15 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0006_auto_20211102_1053'),
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('min', models.IntegerField()),
                ('max', models.IntegerField()),
                ('pincode', models.CharField(max_length=6)),
            ],
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
