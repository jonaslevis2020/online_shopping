# Generated by Django 3.2.5 on 2022-05-07 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, upload_to='media/photos/products'),
        ),
    ]