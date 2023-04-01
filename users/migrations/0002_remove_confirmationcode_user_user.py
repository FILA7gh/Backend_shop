# Generated by Django 4.1.7 on 2023-04-01 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='confirmationcode',
            name='user',
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('code', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.confirmationcode')),
            ],
        ),
    ]