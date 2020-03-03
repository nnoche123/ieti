# Generated by Django 3.0.3 on 2020-03-03 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_student_grades'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='teacher',
        ),
        migrations.AddField(
            model_name='studentsubject',
            name='teacher',
            field=models.ManyToManyField(to='accounts.Teacher'),
        ),
    ]
