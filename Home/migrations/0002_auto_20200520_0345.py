# Generated by Django 3.0.3 on 2020-05-19 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmerupload',
            name='city_dist',
            field=models.CharField(default=2, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='farmerupload',
            name='Address',
            field=models.CharField(max_length=30),
        ),
    ]
