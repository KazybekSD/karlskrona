# Generated by Django 4.2.1 on 2023-05-23 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sma', '0014_alter_indicator_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='indicator',
            name='value',
        ),
    ]