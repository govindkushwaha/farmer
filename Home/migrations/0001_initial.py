# Generated by Django 3.0.3 on 2020-05-19 20:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Farmerupload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(blank=True, upload_to='users/%Y/%m/%d/')),
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
        migrations.CreateModel(
            name='uploadFarmer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
        migrations.CreateModel(
            name='farmer',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Email', models.CharField(max_length=50)),
                ('Occupation', models.CharField(max_length=30)),
                ('Pass', models.CharField(max_length=30)),
                ('CPass', models.CharField(max_length=30)),
                ('Phonenumber', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='buyer',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Email', models.CharField(max_length=50)),
                ('Occupation', models.CharField(max_length=30)),
                ('Pass', models.CharField(max_length=30)),
                ('CPass', models.CharField(max_length=30)),
                ('Phonenumber', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]