#!/usr/bin/env bash
# Build script for Render deployment

set -o errexit  # Exit on error

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --no-input

echo "Running migrations..."
python manage.py migrate

echo "Creating admin user and profile..."
python manage.py shell << 'HEREDOC'
from django.contrib.auth import get_user_model
from core.models import UserProfile, MessSettings

User = get_user_model()

# Create or get admin user
if not User.objects.filter(username='admin').exists():
    print('Creating admin superuser...')
    admin = User.objects.create_superuser(
        username='admin',
        email='pawantripathi802@gmail.com',
        password='admin123'
    )
    print(f'✅ Admin user created: {admin.username}')
else:
    print('ℹ️ Admin user already exists')
    admin = User.objects.get(username='admin')

# Create or update admin profile using get_or_create
profile, created = UserProfile.objects.get_or_create(
    user=admin,
    defaults={
        'phone': '1234567890',
        'role': 'admin'
    }
)
if not created:
    # Update existing profile
    profile.phone = '1234567890'
    profile.role = 'admin'
    profile.save()
    print('✅ Admin profile updated')
else:
    print('✅ Admin profile created')


# Configure UPI payment settings
print('Setting up UPI payment details...')
settings, created = MessSettings.objects.get_or_create(
    pk=1,
    defaults={'max_users': 50}
)
settings.upi_id = 'pawantripathi802@ybl'
settings.upi_qr_code = 'upi_qr/phonepe_qr.jpg'
settings.save()
print(f'✅ UPI ID: {settings.upi_id}')
print(f'✅ QR Code: {settings.upi_qr_code}')

# Create test user
print('Creating test user...')
if not User.objects.filter(username='testuser').exists():
    test_user = User.objects.create_user(
        username='testuser',
        email='testuser@example.com',
        password='test123',
        first_name='Test',
        last_name='User'
    )
    # Create or update test user profile using get_or_create
    profile, created = UserProfile.objects.get_or_create(
        user=test_user,
        defaults={
            'phone': '9999999999',
            'room_no': '101',
            'role': 'user'
        }
    )
    if not created:
        # Update existing profile
        profile.phone = '9999999999'
        profile.room_no = '101'
        profile.role = 'user'
        profile.save()
    print('✅ Test user created: testuser / test123')
else:
    print('ℹ️ Test user already exists')

# Verify admin
print(f'Username: {admin.username}')
print(f'Email: {admin.email}')
print(f'Is superuser: {admin.is_superuser}')
print(f'Is staff: {admin.is_staff}')
print(f'Is active: {admin.is_active}')
admin.set_password('admin123')  # Ensure password is set
admin.save()
print('✅ Admin setup complete!')
HEREDOC

echo "Build complete!"
