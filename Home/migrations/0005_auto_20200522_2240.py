# Generated by Django 3.0.3 on 2020-05-22 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_contactus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmerupload',
            name='Image',
            field=models.ImageField(blank=True, upload_to='static/img'),
        ),
    ]
