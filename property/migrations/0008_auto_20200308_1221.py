# Generated by Django 2.2.4 on 2020-03-08 09:21

from django.db import migrations
from phonenumbers import parse, format_number, PhoneNumberFormat, is_valid_number

def normalaize_phone_number(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        parsed_number = parse(flat.owners_phonenumber, 'RU')
        if is_valid_number(parsed_number):
            flat.owner_phone_pure = format_number(parsed_number, PhoneNumberFormat.E164)
        else:
            flat.owner_phone_pure = None
        flat.save()

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_flat_owner_phone_pure'),
    ]

    operations = [
        migrations.RunPython(normalaize_phone_number),
    ]
