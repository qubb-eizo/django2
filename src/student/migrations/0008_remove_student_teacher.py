# Generated by Django 3.0.6 on 2020-05-21 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_student_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='teacher',
        ),
    ]
