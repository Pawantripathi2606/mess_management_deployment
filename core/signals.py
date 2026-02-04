"""
Signal handlers for the core app
Automatically creates UserProfile when new users are created
"""
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from allauth.account.signals import user_signed_up
from .models import UserProfile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Create UserProfile automatically when a new User is created
    This handles both regular signup and admin-created users
    """
    if created:
        # Check if profile already exists (in case of race condition)
        if not hasattr(instance, 'profile'):
            UserProfile.objects.create(
                user=instance,
                role='user',  # Default role for all new users
                dark_mode=False
            )


@receiver(user_signed_up)
def create_profile_for_social_user(sender, request, user, **kwargs):
    """
    Ensure UserProfile is created for social authentication users
    This is a fallback for allauth social signups
    """
    # Check if profile exists
    if not hasattr(user, 'profile'):
        UserProfile.objects.create(
            user=user,
            role='user',  # Default role for social auth users
            dark_mode=False
        )
        
    # Set first name and last name from social account if available
    sociallogin = kwargs.get('sociallogin')
    if sociallogin:
        # Get extra data from social account
        extra_data = sociallogin.account.extra_data
        
        # Update user's name from Google data
        if not user.first_name and 'given_name' in extra_data:
            user.first_name = extra_data.get('given_name', '')
        
        if not user.last_name and 'family_name' in extra_data:
            user.last_name = extra_data.get('family_name', '')
        
        if user.first_name or user.last_name:
            user.save()
