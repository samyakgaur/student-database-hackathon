# Generated by Django 2.2.4 on 2019-08-31 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('first_app', '0009_auto_20190831_0656'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrie',
            name='credits',
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='None', max_length=200)),
                ('marks', models.IntegerField(default=0, null=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
    ]