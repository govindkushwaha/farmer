# Generated by Django 3.0.3 on 2020-05-22 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_auto_20200522_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfarmer',
            name='Email',
            field=models.CharField(max_length=35),
        ),
    ]
