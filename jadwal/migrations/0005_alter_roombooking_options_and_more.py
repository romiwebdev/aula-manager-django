# Generated by Django 5.1.3 on 2024-11-24 04:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jadwal', '0004_rentalprice_roombooking_total_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='roombooking',
            options={},
        ),
        migrations.RemoveField(
            model_name='roombooking',
            name='bank_account_number',
        ),
        migrations.RemoveField(
            model_name='roombooking',
            name='total_price',
        ),
        migrations.AddField(
            model_name='roombooking',
            name='rental_price',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jadwal.rentalprice'),
        ),
        migrations.AlterField(
            model_name='roombooking',
            name='customer_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='roombooking',
            name='organization',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='roombooking',
            name='password',
            field=models.CharField(max_length=200),
        ),
    ]
