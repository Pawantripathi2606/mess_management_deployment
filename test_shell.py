from django.contrib.auth.models import User
from core.models import UserProfile
from core.forms import UserRegistrationForm

# Clean up test user
try:
    User.objects.get(username='test999').delete()
except:
    pass

# Create user via form
form_data = {
    'username': 'test999',
    'first_name': 'Test',
    'last_name': 'User',
    'email': 'test999@test.com',
    'password1': 'TestPass123!',
    'password2': 'TestPass123!',
    'phone': '1234567890',
    'room_no': '999',
    'role': 'user'
}

form = UserRegistrationForm(form_data)
if form.is_valid():
    user = form.save()
    print(f"User created: {user.username}")
    profile_count = UserProfile.objects.filter(user=user).count()
    print(f"Profile count: {profile_count}")
    if profile_count == 1:
        print("SUCCESS - Only one profile created")
        profile = user.userprofile
        print(f"Role: {profile.role}, Phone: {profile.phone}, Room: {profile.room_no}")
    else:
        print(f"ERROR - {profile_count} profiles created")
else:
    print("Form errors:", form.errors)
