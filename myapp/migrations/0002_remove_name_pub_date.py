# Generated by Django 3.2.3 on 2023-03-03 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='name',
            name='pub_date',
        ),
    ]
