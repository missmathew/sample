# Generated by Django 5.0.2 on 2024-06-24 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_customer_confirm_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='confirm_password',
            new_name='confirmpassword',
        ),
    ]
