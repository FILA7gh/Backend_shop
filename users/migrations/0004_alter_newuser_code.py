# Generated by Django 4.1.7 on 2023-04-01 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_newuser_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='code',
            field=models.CharField(max_length=6),
        ),
    ]
