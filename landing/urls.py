from django.urls import path
from . import views
from .views import landing_home, export_template

from django.urls import path
from .views import landing_home, export_template, demo_view
from landing.views import landing_home


urlpatterns = [
    path('', landing_home, name='landing_home'),
    path('export-template/', export_template, name='export_template'),
    path("demo/", demo_view, name="demo_view"),
    path("info/", views.info_page, name="info"),


]
