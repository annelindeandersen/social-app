# Generated by Django 3.0 on 2019-12-07 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialfeedapp', '0003_auto_20191207_1953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedpost',
            name='status',
        ),
    ]