# Generated by Django 4.2.7 on 2024-01-31 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone_number',
            field=models.CharField(default='fdsfdsf', max_length=15),
            preserve_default=False,
        ),
    ]
