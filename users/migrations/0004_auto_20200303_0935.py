# Generated by Django 3.0.3 on 2020-03-03 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200303_0932'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='Ave',
            new_name='FirstSemAve',
        ),
        migrations.AddField(
            model_name='student',
            name='SecondSemAve',
            field=models.IntegerField(null=True, verbose_name=range(70, 95)),
        ),
    ]
