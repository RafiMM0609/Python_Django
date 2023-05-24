# Generated by Django 4.2.1 on 2023-05-24 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_darah', '0002_remove_pengguna_id_pengguna_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='pengguna',
            name='golongan_darah',
            field=models.CharField(default=1, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pengguna',
            name='nomor_hp',
            field=models.IntegerField(default=1, max_length=14),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pengguna',
            name='pekerjaan',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]