# Generated by Django 3.0.6 on 2020-05-07 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_auto_20200506_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
    ]