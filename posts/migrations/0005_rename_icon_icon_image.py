# Generated by Django 4.2.3 on 2023-07-07 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_icon_icon_alter_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='icon',
            old_name='icon',
            new_name='image',
        ),
    ]
