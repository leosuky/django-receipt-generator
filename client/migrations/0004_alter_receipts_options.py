# Generated by Django 3.2.9 on 2021-12-01 00:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_rename_org_number_client_phone'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='receipts',
            options={'ordering': ('-created_at',)},
        ),
    ]
