# Generated by Django 3.1.3 on 2021-06-30 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0005_auto_20210630_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='lesson_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.course'),
        ),
    ]
