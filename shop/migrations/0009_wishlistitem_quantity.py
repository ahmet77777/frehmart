# Generated by Django 4.2.7 on 2024-02-07 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_remove_wishlistitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlistitem',
            name='quantity',
            field=models.SmallIntegerField(default=0),
        ),
    ]
