# Generated by Django 4.1.2 on 2022-10-06 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0016_teacher_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='user',
        ),
    ]
