# Generated by Django 4.2.7 on 2023-11-25 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='ticket_id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
