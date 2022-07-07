# config.urls.py

from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('tasks.urls', namespace='tasks')),
    path(settings.ADMIN_URL, admin.site.urls),
]
