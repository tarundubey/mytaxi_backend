# Generated by Django 2.1.4 on 2019-02-17 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi_ride', '0002_auto_20190216_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='latitude',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='request',
            name='longitude',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
