# anthro_app/urls.py
from django.contrib import admin
from django.urls import path, include
from landing.views import demo_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing.urls')),
    path('panel/', include('admin_panel.urls')),
    path("demo/", demo_view, name="demo_view"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
