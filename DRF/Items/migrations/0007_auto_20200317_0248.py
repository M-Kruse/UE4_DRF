# Generated by Django 3.0.4 on 2020-03-17 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Items', '0006_auto_20200317_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='owner_uuid',
            field=models.UUIDField(blank=True),
        ),
    ]
