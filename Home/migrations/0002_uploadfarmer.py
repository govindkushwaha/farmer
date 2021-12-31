# Generated by Django 3.0.3 on 2020-05-17 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='uploadFarmer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img')),
                ('Name', models.CharField(max_length=20)),
                ('contact', models.IntegerField()),
                ('Address', models.TextField()),
                ('state_country', models.CharField(max_length=20)),
                ('Occupation', models.CharField(max_length=20)),
                ('ProduceName', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=20)),
                ('TotQuantity', models.CharField(max_length=20)),
                ('Quality', models.CharField(max_length=20)),
                ('Category', models.CharField(max_length=50)),
                ('Price_Kg', models.IntegerField()),
            ],
        ),
    ]
