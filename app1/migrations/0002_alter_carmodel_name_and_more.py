# Generated by Django 4.1.7 on 2023-02-21 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='identification_number',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='syndic',
            name='contact_number',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='syndic',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='syndic',
            name='license_number',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='syndic',
            name='surname',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
