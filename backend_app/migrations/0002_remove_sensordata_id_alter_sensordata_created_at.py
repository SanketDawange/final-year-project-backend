# Generated by Django 4.2.1 on 2024-02-27 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensordata',
            name='id',
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='created_at',
            field=models.DateTimeField(primary_key=True, serialize=False),
        ),
    ]
