"""
Test script to verify user creation fix
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mess_management.settings')
django.setup()

from django.contrib.auth.models import User
from core.models import UserProfile
from core.forms import UserRegistrationForm

def test_user_creation():
    print("=" * 60)
    print("TESTING USER CREATION FIX")
    print("=" * 60)
    
    test_username = "testuser_fix_456"
    
    # Clean up if test user exists
    try:
        existing_user = User.objects.get(username=test_username)
        print(f"\nCleaning up existing test user: {test_username}")
        existing_user.delete()
    except User.DoesNotExist:
        pass
    
    # Create form data
    form_data = {
        'username': test_username,
        'first_name': 'Test',
        'last_name': 'User',
        'email': 'testuser@example.com',
        'password1': 'SecurePass123!',
        'password2': 'SecurePass123!',
        'phone': '9876543210',
        'room_no': '101',
        'role': 'user'
    }
    
    print(f"\nCreating user: {form_data['username']}")
    
    # Create user using form
    form = UserRegistrationForm(form_data)
    
    if form.is_valid():
        try:
            user = form.save()
            print(f"SUCCESS: User created - ID: {user.id}")
            
            # Verify UserProfile
            try:
                profile = user.userprofile
                print(f"SUCCESS: UserProfile found - ID: {profile.id}")
                print(f"         Role: {profile.role}")
                print(f"         Phone: {profile.phone}")
                print(f"         Room: {profile.room_no}")
                
                # Check profile count
                profile_count = UserProfile.objects.filter(user=user).count()
                print(f"\nUserProfile count: {profile_count}")
                
                if profile_count == 1:
                    print("PASS: Exactly one UserProfile exists")
                else:
                    print(f"FAIL: {profile_count} UserProfiles exist (expected 1)")
                
                # Verify data
                if (profile.role == form_data['role'] and 
                    profile.phone == form_data['phone'] and 
                    profile.room_no == form_data['room_no']):
                    print("PASS: Profile data matches form data")
                else:
                    print("FAIL: Profile data mismatch")
                    
            except UserProfile.DoesNotExist:
                print("FAIL: UserProfile not created")
                
        except Exception as e:
            print(f"\nERROR: {type(e).__name__}")
            print(f"Message: {str(e)}")
            
            if "UNIQUE constraint failed" in str(e):
                print("FAIL: IntegrityError - Profile created twice")
            
    else:
        print("FAIL: Form validation failed")
        for field, errors in form.errors.items():
            print(f"  {field}: {errors}")
    
    print("\n" + "=" * 60)
    print("TEST COMPLETE")
    print("=" * 60)

if __name__ == '__main__':
    test_user_creation()
