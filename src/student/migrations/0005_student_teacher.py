# Generated by Django 3.0.6 on 2020-05-21 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
        ('student', '0004_auto_20200521_0839'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='teacher',
            field=models.ManyToManyField(related_name='students', to='teacher.Teacher'),
        ),
    ]
