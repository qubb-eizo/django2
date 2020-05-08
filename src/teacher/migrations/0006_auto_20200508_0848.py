# Generated by Django 3.0.6 on 2020-05-08 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0005_auto_20200508_0841'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='teacher',
            name='name of constraint',
        ),
        migrations.AddConstraint(
            model_name='teacher',
            constraint=models.UniqueConstraint(fields=('first_name', 'last_name'), name='name of constraint teachers'),
        ),
    ]
