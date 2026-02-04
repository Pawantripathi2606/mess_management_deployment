"""
Test script to verify user creation fix
This tests that UserProfile is created only once without IntegrityError
"""
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mess_management.settings')
django.setup()

from django.contrib.auth.models import User
from core.models import UserProfile
from core.forms import UserRegistrationForm

def test_user_creation():
    """Test user creation through the form"""
    print("=" * 60)
    print("TESTING USER CREATION FIX")
    print("=" * 60)
    
    # Test data
    test_username = "testuser_fix_123"
    
    # Clean up if test user exists
    try:
        existing_user = User.objects.get(username=test_username)
        print(f"\n🧹 Cleaning up existing test user: {test_username}")
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
    
    print(f"\n📝 Creating user with form data:")
    print(f"   Username: {form_data['username']}")
    print(f"   Name: {form_data['first_name']} {form_data['last_name']}")
    print(f"   Email: {form_data['email']}")
    print(f"   Phone: {form_data['phone']}")
    print(f"   Room: {form_data['room_no']}")
    print(f"   Role: {form_data['role']}")
    
    # Create user using form
    form = UserRegistrationForm(form_data)
    
    if form.is_valid():
        try:
            user = form.save()
            print(f"\n✅ User created successfully!")
            print(f"   User ID: {user.id}")
            print(f"   Username: {user.username}")
            
            # Verify UserProfile was created
            try:
                profile = user.userprofile
                print(f"\n✅ UserProfile found!")
                print(f"   Profile ID: {profile.id}")
                print(f"   Role: {profile.role}")
                print(f"   Phone: {profile.phone}")
                print(f"   Room No: {profile.room_no}")
                
                # Check that only ONE profile exists for this user
                profile_count = UserProfile.objects.filter(user=user).count()
                print(f"\n📊 UserProfile count for this user: {profile_count}")
                
                if profile_count == 1:
                    print("✅ SUCCESS: Exactly one UserProfile exists (correct!)")
                else:
                    print(f"❌ ERROR: {profile_count} UserProfiles exist (should be 1)")
                
                # Verify profile data matches form data
                if (profile.role == form_data['role'] and 
                    profile.phone == form_data['phone'] and 
                    profile.room_no == form_data['room_no']):
                    print("✅ SUCCESS: Profile data matches form data")
                else:
                    print("❌ ERROR: Profile data does not match form data")
                    print(f"   Expected role: {form_data['role']}, Got: {profile.role}")
                    print(f"   Expected phone: {form_data['phone']}, Got: {profile.phone}")
                    print(f"   Expected room: {form_data['room_no']}, Got: {profile.room_no}")
                
            except UserProfile.DoesNotExist:
                print("\n❌ ERROR: UserProfile was not created!")
                
        except Exception as e:
            print(f"\n❌ ERROR during user creation:")
            print(f"   Type: {type(e).__name__}")
            print(f"   Message: {str(e)}")
            
            if "UNIQUE constraint failed" in str(e):
                print("\n⚠️  IntegrityError detected! The fix is NOT working.")
                print("   UserProfile is still being created twice.")
            
    else:
        print(f"\n❌ Form validation failed:")
        for field, errors in form.errors.items():
            print(f"   {field}: {', '.join(errors)}")
    
    print("\n" + "=" * 60)
    print("TEST COMPLETE")
    print("=" * 60)

if __name__ == '__main__':
    test_user_creation()
