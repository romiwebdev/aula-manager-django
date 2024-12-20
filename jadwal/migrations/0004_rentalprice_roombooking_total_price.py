# Generated by Django 5.1.3 on 2024-11-24 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jadwal', '0003_remove_roombooking_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RentalPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_type', models.CharField(choices=[('weekday', 'Senin - Jumat'), ('weekend', 'Sabtu - Minggu')], max_length=10)),
                ('price_per_hour', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.AddField(
            model_name='roombooking',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
