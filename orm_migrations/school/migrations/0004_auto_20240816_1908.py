# Generated by Django 3.2.25 on 2024-08-16 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_teacherstudent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='teacher',
        ),
        migrations.AddField(
            model_name='student',
            name='teachers',
            field=models.ManyToManyField(related_name='teacher', to='school.Teacher'),
        ),
        migrations.DeleteModel(
            name='TeacherStudent',
        ),
    ]
