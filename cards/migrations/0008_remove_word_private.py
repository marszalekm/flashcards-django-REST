# Generated by Django 3.1.1 on 2020-10-07 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0007_auto_20201007_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='private',
        ),
    ]
