# Generated by Django 4.2.6 on 2024-01-10 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='list',
            options={'ordering': ['title']},
        ),
    ]
