# Generated by Django 4.2.15 on 2024-08-31 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='firstName',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='lastName',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='motto',
            field=models.CharField(default='', max_length=100),
        ),
    ]