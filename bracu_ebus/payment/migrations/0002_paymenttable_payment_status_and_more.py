# Generated by Django 4.2.7 on 2023-11-30 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymenttable',
            name='payment_status',
            field=models.CharField(default='pending', max_length=20),
        ),
        migrations.AddField(
            model_name='paymenttable',
            name='token_number',
            field=models.CharField(default='', max_length=255),
        ),
    ]
