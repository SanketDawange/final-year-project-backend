# Generated by Django 4.2.1 on 2024-03-25 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0003_alter_sensordata_entry_id_alter_sensordata_field1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alert_message', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
