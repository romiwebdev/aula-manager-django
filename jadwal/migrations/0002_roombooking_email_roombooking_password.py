# Generated by Django 5.1.3 on 2024-11-24 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jadwal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='roombooking',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
        migrations.AddField(
            model_name='roombooking',
            name='password',
            field=models.CharField(default='defaultpassword123', max_length=50),
        ),
    ]
