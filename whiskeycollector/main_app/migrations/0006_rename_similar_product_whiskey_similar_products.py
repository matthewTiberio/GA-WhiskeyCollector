# Generated by Django 4.1.3 on 2022-11-14 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_rename_similiar_product_whiskey_similar_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='whiskey',
            old_name='similar_product',
            new_name='similar_products',
        ),
    ]
