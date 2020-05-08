# Generated by Django 3.0.6 on 2020-05-07 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_auto_20200507_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='email',
            field=models.EmailField(max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='phone_number',
            field=models.CharField(default=380000000000, max_length=12, unique=True),
        ),
    ]