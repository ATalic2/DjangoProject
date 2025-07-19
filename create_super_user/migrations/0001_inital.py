from django.contrib.auth.hashers import make_password
from django.db import migrations, models

def create_initial_users(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    User.objects.create(
        username='admin',
        password=make_password('admin123'),  # hash it manually
        is_staff=True,
        is_superuser=True,
    )
    User.objects.create(
        username='user1',
        password=make_password('userpass'),
        is_staff=False,
        is_superuser=False,
    )

class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),  # may differ
    ]

    operations = [
        migrations.RunPython(create_initial_users),
    ]
