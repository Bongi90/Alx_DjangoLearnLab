from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda user: user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin')
def admin_view(request):
    """
    View accessible only to users with the 'Admin' role.
    """
    return render(request, 'relationship_app/admin_view.html')
