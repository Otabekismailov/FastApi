# Generated by Django 4.2.1 on 2023-05-15 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]