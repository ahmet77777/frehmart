# Generated by Django 4.2.7 on 2024-02-02 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_order_phone_number'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]
