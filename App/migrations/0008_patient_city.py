# Generated by Django 3.2.12 on 2022-04-09 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='city',
            field=models.CharField(default='Jodhpur', max_length=50),
        ),
    ]