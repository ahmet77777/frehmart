# Generated by Django 4.2.7 on 2024-01-20 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='status',
            field=models.SmallIntegerField(default=0),
        ),
    ]