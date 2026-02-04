"""
Django shell script to set up UPI payment details with PhonePe QR code
Run with: python manage.py shell < setup_upi.py
"""

from core.models import MessSettings

# Get or create settings
settings, created = MessSettings.objects.get_or_create(
    pk=1,
    defaults={
        'max_users': 50,
    }
)

# Update UPI details
settings.upi_id = 'pawantripathi802@ybl'  # Update with your actual UPI ID
settings.upi_qr_code = 'upi_qr/phonepe_qr.jpg'
settings.save()

print('✅ UPI Settings Updated!')
print(f'UPI ID: {settings.upi_id}')
print(f'QR Code: {settings.upi_qr_code}')
