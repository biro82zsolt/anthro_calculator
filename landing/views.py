from django.shortcuts import render
from django.http import FileResponse
import os
from django.conf import settings
import pandas as pd

from anthro_app.utils import process_dataframe
from admin_panel.utils import export_dataframe_to_excel
from admin_panel.views import generate_height_chart


def demo_view(request):
    demo_file_path = os.path.join(settings.BASE_DIR, "static", "demo_data.csv")
    df = pd.read_csv(demo_file_path, sep=";", decimal=",", encoding="utf-8")
    df_processed = process_dataframe(df)

    excel_path = export_dataframe_to_excel(df_processed)
    excel_filename = os.path.basename(excel_path)
    chart_filename = generate_height_chart(df_processed)

    return render(request, "landing/demo.html", {
        "chart": chart_filename,
        "excel_path": excel_filename
    })

def landing_home(request):
    return render(request, "landing/home.html")

def export_template(request):
    template_path = os.path.join(settings.BASE_DIR, "static", "template.xlsx")
    if os.path.exists(template_path):
        return FileResponse(open(template_path, 'rb'), as_attachment=True, filename="ures_sablon.xlsx")
    else:
        raise Http404("A sablon fájl nem található.")

def info_page(request):
    return render(request, "landing/info.html")