# Generated by Django 3.2.25 on 2024-08-24 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20240824_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(related_name='tag', through='articles.Score', to='articles.Tag'),
        ),
    ]
