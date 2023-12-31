# Generated by Django 4.2.2 on 2023-10-09 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0005_student'),
        ('Quiz', '0025_remove_result_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='score',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='result',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_results', to='Quiz.quiz'),
        ),
        migrations.AlterField(
            model_name='result',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_results', to='signup.student'),
        ),
    ]
