from django.db import migrations

def create_initial_clients(apps, schema_editor):
    Client = apps.get_model('client', 'Client')
    Merchant = apps.get_model('merchant', 'Merchant')
    Client.objects.create(firstName='TestName1', lastName='TestSurname1', job='Job1', merchant=Merchant.objects.get(id=1))
    Client.objects.create(firstName='TestName2', lastName='TestSurname2', job='Job2', merchant=Merchant.objects.get(id=1))
    Client.objects.create(firstName='TestName3', lastName='TestSurname3', job='Job3', merchant=Merchant.objects.get(id=2))

class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
        ('merchant', '0001_initial'),
        ('merchant', '0002_populate_merchants'),
        ('client', '0003_client_merchant')
    ]

    operations = [
        migrations.RunPython(create_initial_clients),
    ]
