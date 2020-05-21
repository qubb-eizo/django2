# Generated by Django 3.0.6 on 2020-05-21 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
        ('student', '0006_remove_student_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='teacher',
            field=models.ManyToManyField(null=True, related_name='students', to='teacher.Teacher'),
        ),
    ]
