# Generated by Django 3.2.9 on 2021-12-03 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_auto_20211202_1833'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='agency',
            new_name='author',
        ),
    ]
