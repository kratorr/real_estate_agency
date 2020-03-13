# Generated by Django 2.2.4 on 2020-03-11 19:35

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20200309_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='owner_phone_pure',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, db_index=True, max_length=128, null=True, region=None, verbose_name='Нормализованный номер владельца'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owner_phonenumber',
            field=models.CharField(db_index=True, max_length=20, null=True, verbose_name='Номер владельца'),
        ),
    ]