from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('items.urls', namespace='items')),
    path('admin/', admin.site.urls),
]
