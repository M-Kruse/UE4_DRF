# Generated by Django 3.0.4 on 2020-03-16 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Items', '0003_auto_20200316_0114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='owner',
            new_name='owner_uuid',
        ),
    ]
