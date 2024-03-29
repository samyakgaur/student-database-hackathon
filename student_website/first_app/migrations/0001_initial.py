# Generated by Django 2.2.4 on 2019-08-30 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=264, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Entries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264, unique=True)),
                ('title', models.CharField(max_length=264, unique=True)),
                ('description', models.TextField(blank=True, max_length=600, null=True)),
                ('url', models.URLField(unique=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('year', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], default=1)),
                ('department', models.CharField(choices=[('Computers', 'Computers'), ('IT', 'IT'), ('Electronics', 'Electronics'), ('Production', 'Production'), ('Mechanical', 'Mechanical')], default='Computer', max_length=100)),
                ('research_paper', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=100)),
                ('credits', models.IntegerField(default=0, null=True)),
                ('topics', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='first_app.Topic')),
            ],
        ),
    ]
