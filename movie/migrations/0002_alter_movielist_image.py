# Generated by Django 4.0.4 on 2022-12-19 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movielist',
            name='image',
            field=models.TextField(blank=True, null=True),
        ),
    ]
