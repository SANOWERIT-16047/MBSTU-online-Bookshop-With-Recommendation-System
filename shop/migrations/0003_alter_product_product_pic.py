# Generated by Django 4.1 on 2022-10-25 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_genres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_pic',
            field=models.ImageField(default='book-default.jpg', upload_to='product'),
        ),
    ]