from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ctf.urls')),  # Include the URLs from the 'ctf' app
]