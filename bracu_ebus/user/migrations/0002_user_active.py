# Generated by Django 4.2.7 on 2023-11-16 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='active',
            field=models.CharField(default=False, max_length=10),
        ),
    ]