# Generated by Django 3.2.3 on 2023-03-03 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_name_pub_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='name',
            old_name='name',
            new_name='user',
        ),
    ]
