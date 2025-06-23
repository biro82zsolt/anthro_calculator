from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("upload-csv/", views.upload_csv, name="upload_csv"),
    path("export-csv/", views.export_csv, name="export_csv"),
    path("export-excel/", views.export_excel, name="export_excel"),
    path("download-template/", views.download_template, name="download_template"),
]
