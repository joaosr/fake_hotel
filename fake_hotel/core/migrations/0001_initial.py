# Generated by Django 2.2.6 on 2019-10-22 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_in', models.DateField(blank=True, null=True, verbose_name='Date In')),
                ('date_out', models.DateField(blank=True, null=True, verbose_name='Date Out')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
        ),
    ]
