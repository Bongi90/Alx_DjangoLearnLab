from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # This line tells Django to look for more URL patterns in your api app.
    path('api/', include('api.urls')),
]
