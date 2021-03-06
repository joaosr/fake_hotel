# Generated by Django 2.2.6 on 2019-11-02 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_reservation_guest_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('max_capacity', models.IntegerField(default=1, verbose_name='Max Capacity')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='room_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.RoomType'),
            preserve_default=False,
        ),
    ]
