# Generated by Django 4.2.7 on 2024-01-18 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subcategory', '0003_alter_subcategory_icon_alter_subcategory_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('new_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('old_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('create_at', models.DateTimeField()),
                ('update_at', models.DateTimeField()),
                ('image', models.ImageField(upload_to='products/')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_of_subcategory', to='subcategory.subcategory')),
            ],
        ),
    ]
