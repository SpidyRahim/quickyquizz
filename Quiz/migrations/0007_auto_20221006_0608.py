# Generated by Django 3.0.5 on 2022-10-06 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0006_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Quiz.Quiz'),
        ),
    ]
