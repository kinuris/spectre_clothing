# Generated by Django 5.2.1 on 2025-05-21 04:00

from django.db import migrations
from django.contrib.auth.hashers import make_password


def create_default_staff(apps, schema_editor):
    # Get the user model from the app registry
    User = apps.get_model('accounts', 'User')
    
    # Create default stock manager if it doesn't exist
    if not User.objects.filter(username='stockmanager').exists():
        User.objects.create(
            username='stockmanager',
            email='inventory@spectrastore.com',
            password=make_password('StockPassword123!'),
            first_name='Inventory',
            last_name='Manager',
            is_staff=True,
            is_active=True,
            role='stock_manager'
        )
    
    # Create default sales staff if it doesn't exist
    if not User.objects.filter(username='salesstaff').exists():
        User.objects.create(
            username='salesstaff',
            email='sales@spectrastore.com',
            password=make_password('SalesPassword123!'),
            first_name='Sales',
            last_name='Associate',
            is_staff=True,
            is_active=True,
            role='sales'
        )


def reverse_default_staff(apps, schema_editor):
    # Get the user model from the app registry
    User = apps.get_model('accounts', 'User')
    
    # Delete the default staff users if they exist
    User.objects.filter(username='stockmanager').delete()
    User.objects.filter(username='salesstaff').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_create_default_user'),
    ]

    operations = [
        migrations.RunPython(
            create_default_staff,
            reverse_default_staff
        ),
    ]
