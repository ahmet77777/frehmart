# Generated by Django 4.2.7 on 2024-02-10 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subcategory', '0004_alter_subcategory_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='subcategory/'),
        ),
    ]