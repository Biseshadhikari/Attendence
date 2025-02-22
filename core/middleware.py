# middleware/first_time_password_change.py
from django.shortcuts import redirect
from django.urls import reverse

class FirstTimePasswordChangeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            # Ensure the user has a profile
            if not hasattr(request.user, 'profile'):
                from core.models import Profile
                Profile.objects.create(user=request.user)  # Create profile if it doesn't exist

            # Allow access to password change and logout pages
            allowed_paths = [reverse('password_change'), reverse('logout')]

            # Check if password has been changed
            if not request.user.profile.password_changed and request.path not in allowed_paths:
                return redirect('password_change')

        response = self.get_response(request)
        return response
