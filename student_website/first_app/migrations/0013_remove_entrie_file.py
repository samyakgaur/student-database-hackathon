# Generated by Django 2.2.2 on 2019-09-07 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0012_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrie',
            name='file',
        ),
    ]
