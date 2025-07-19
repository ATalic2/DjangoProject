from django.db import migrations

def create_initial_merchants(apps, schema_editor):
    Merchant = apps.get_model('merchant', 'Merchant')
    Merchant.objects.create(name='Amazon')
    Merchant.objects.create(name='eBay')
    Merchant.objects.create(name='Walmart')

class Migration(migrations.Migration):

    dependencies = [
        ('merchant', '0001_initial'),  # Make sure this matches your previous migration
    ]

    operations = [
        migrations.RunPython(create_initial_merchants),
    ]
