# Generated by Django 2.2.4 on 2019-08-31 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entries',
            name='file',
            field=models.FileField(default='NULL', upload_to=None),
        ),
    ]