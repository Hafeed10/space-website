from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static  # Add this import for serving media files

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("web.urls", namespace="web")),  # Correct the include syntax
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
