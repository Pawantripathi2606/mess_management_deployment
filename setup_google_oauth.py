"""
Google OAuth Admin Setup Helper
================================
Run this script to quickly configure Sites and Social Application for Google OAuth.

This script:
1. Updates the Site domain to 127.0.0.1:8000
2. Creates a Google Social Application with your credentials
3. Links the Social App to the Site

Requirements:
- Django admin superuser must already exist
- Migrations must be completed
"""

import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mess_management.settings')
django.setup()

from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp

def setup_google_oauth():
    """Configure Sites and Google OAuth Social Application"""
    
    print("=" * 60)
    print("Google OAuth Setup Helper")
    print("=" * 60)
    
    # Step 1: Update Site
    print("\n[1/2] Configuring Sites framework...")
    site, created = Site.objects.get_or_create(id=1)
    site.domain = '127.0.0.1:8000'
    site.name = 'Mess Management System'
    site.save()
    
    if created:
        print("✅ Created new Site: 127.0.0.1:8000")
    else:
        print("✅ Updated existing Site: 127.0.0.1:8000")
    
    # Step 2: Create Google Social Application
    print("\n[2/2] Setting up Google OAuth application...")
    
    # Load Google OAuth credentials from environment variables
    CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
    CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
    
    if not CLIENT_ID or not CLIENT_SECRET:
        print("\n❌ Error: Google OAuth credentials not found!")
        print("\nPlease set the following environment variables:")
        print("  GOOGLE_CLIENT_ID=your-client-id.apps.googleusercontent.com")
        print("  GOOGLE_CLIENT_SECRET=your-client-secret")
        print("\nYou can:")
        print("  1. Create a .env file with the credentials (see .env.example)")
        print("  2. Or set them as system environment variables")
        print("\nGet your credentials from: https://console.cloud.google.com/apis/credentials")
        return False
    
    # Create or update Social App
    social_app, created = SocialApp.objects.get_or_create(
        provider='google',
        name='Google OAuth',
        defaults={
            'client_id': CLIENT_ID,
            'secret': CLIENT_SECRET,
        }
    )
    
    if not created:
        # Update existing app
        social_app.client_id = CLIENT_ID
        social_app.secret = CLIENT_SECRET
        social_app.save()
        print("✅ Updated existing Google OAuth application")
    else:
        print("✅ Created new Google OAuth application")
    
    # Link to site
    if site not in social_app.sites.all():
        social_app.sites.add(site)
        print("✅ Linked Google OAuth to site")
    else:
        print("✅ Google OAuth already linked to site")
    
    print("\n" + "=" * 60)
    print("✅ Setup Complete!")
    print("=" * 60)
    
    print("\n📋 Configuration Summary:")
    print(f"   Site Domain: {site.domain}")
    print(f"   Site Name: {site.name}")
    print(f"   OAuth Provider: Google")
    print(f"   OAuth App Name: {social_app.name}")
    print(f"   Client ID: {social_app.client_id[:20]}...")
    
    print("\n🔧 Next Steps:")
    print("   1. Start the server: python manage.py runserver")
    print("   2. Visit: http://127.0.0.1:8000/accounts/login/")
    print("   3. Click 'Continue with Google' to test")
    
    print("\n⚠️  IMPORTANT - Google Cloud Console:")
    print("   Add this redirect URI to your Google Cloud Console:")
    print("   http://127.0.0.1:8000/accounts/google/login/callback/")
    print("\n")
    
    return True

if __name__ == '__main__':
    try:
        setup_google_oauth()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nMake sure you have:")
        print("  1. Run migrations: python manage.py migrate")
        print("  2. Created a superuser: python manage.py createsuperuser")
