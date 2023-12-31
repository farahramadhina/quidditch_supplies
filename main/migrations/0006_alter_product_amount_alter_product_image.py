# Generated by Django 4.2.5 on 2023-09-29 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default=1, upload_to='media/'),
            preserve_default=False,
        ),
    ]
