# Generated by Django 3.0.3 on 2020-03-03 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200303_0418'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='subject',
            field=models.ManyToManyField(through='accounts.StudentSubject', to='accounts.Subject'),
        ),
        migrations.AlterField(
            model_name='student',
            name='grades',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='grade', to='accounts.Subject'),
        ),
        migrations.RemoveField(
            model_name='studentsubject',
            name='student',
        ),
        migrations.AddField(
            model_name='studentsubject',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.Student'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='studentsubject',
            name='subject',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.Subject'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
