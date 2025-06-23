# anthro_app/urls.py
from django.contrib import admin
from django.urls import path, include
from landing.views import demo_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing.urls')),
    path('panel/', include('admin_panel.urls')),
    path("demo/", demo_view, name="demo_view"),
]
