# Generated by Django 3.2.12 on 2022-03-02 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_auto_20220303_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='time',
            field=models.DateField(auto_now=True),
        ),
    ]