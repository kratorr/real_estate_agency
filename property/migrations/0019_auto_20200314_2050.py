# Generated by Django 2.2.4 on 2020-03-14 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0018_auto_20200313_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='new_building',
            field=models.NullBooleanField(db_index=True, verbose_name='Новостройка'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='flats',
            field=models.ManyToManyField(related_name='owners', to='property.Flat', verbose_name='Квартиры в собественности'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='name',
            field=models.CharField(default='', max_length=200, verbose_name='ФИО владельца'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owner_phonenumber',
            field=models.CharField(db_index=True, default='', max_length=20, verbose_name='Номер владельца'),
        ),
    ]
