# Generated by Django 3.0.6 on 2020-05-21 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0003_auto_20200520_1716'),
        ('student', '0003_auto_20200520_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='group.Group'),
        ),
    ]
