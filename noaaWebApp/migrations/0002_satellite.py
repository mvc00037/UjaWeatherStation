# Generated by Django 4.1.1 on 2022-09-07 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noaaWebApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Satellite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name_plural': 'Satellite',
            },
        ),
    ]
