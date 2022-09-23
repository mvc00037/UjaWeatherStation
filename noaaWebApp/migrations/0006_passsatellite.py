# Generated by Django 4.1.1 on 2022-09-16 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noaaWebApp', '0005_delete_idsatellite'),
    ]

    operations = [
        migrations.CreateModel(
            name='passSatellite',
            fields=[
                ('noradId', models.IntegerField(primary_key=True, serialize=False)),
                ('satname', models.CharField(max_length=50)),
                ('transactionscount', models.IntegerField()),
                ('startAz', models.CharField(max_length=25)),
                ('endAz', models.CharField(max_length=25)),
                ('startUTC', models.CharField(max_length=75)),
                ('endUTC', models.CharField(max_length=25)),
                ('maxEl', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name_plural': 'passSatellite',
            },
        ),
    ]
