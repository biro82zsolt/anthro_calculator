import os
import csv
import io
import pandas as pd
import matplotlib.pyplot as plt
import time

from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect, FileResponse
from django.urls import reverse
from django.conf import settings

from anthro_app.utils import process_dataframe
from admin_panel.utils import export_dataframe_to_excel


def demo_view(request):
    demo_file_path = os.path.join(settings.BASE_DIR, "static", "demo_data.csv")
    if not os.path.exists(demo_file_path):
        return HttpResponse("Demó adatfájl nem található.", status=404)

    df = pd.read_csv(demo_file_path, sep=";", decimal=",", encoding="utf-8")
    df_processed = process_dataframe(df)

    excel_path = export_dataframe_to_excel(df_processed)
    excel_filename = os.path.basename(excel_path)
    chart_filename = generate_height_chart(df_processed)

    return render(request, "landing/demo.html", {
        "chart": chart_filename,
        "excel_path": excel_filename
    })


def home(request):
    return render(request, "admin_panel/home.html")


def upload_csv(request):
    if request.method == "POST" and request.FILES.get("file"):
        try:
            file = request.FILES["file"]
            text = file.read().decode("utf-8-sig")

            df = pd.read_csv(
                io.StringIO(text),
                sep=";",
                decimal=",",
                quotechar='"',
                skip_blank_lines=True,
                engine="python",
                on_bad_lines="skip",
                header=0
            ).dropna(how="all")

            if df.empty or df.columns.size == 0:
                messages.error(request, "A CSV fájl üres vagy nem tartalmaz oszlopokat.")
                return HttpResponseRedirect(request.path)

            required_cols = {"név", "testmagasság", "neme"}
            if not required_cols.issubset(df.columns):
                messages.error(request, "Hiányzó kötelező oszlop(ok): 'név', 'testmagasság', 'neme'.")
                return HttpResponseRedirect(request.path)

            df_processed = process_dataframe(df)
            export_path = export_dataframe_to_excel(df_processed)
            export_filename = os.path.basename(export_path)
            chart_filename = generate_height_chart(df_processed)

            messages.success(request, "Fájl sikeresen feldolgozva.")
            return render(
                request,
                "admin_panel/chart.html",
                {"excel_path": export_filename, "chart": chart_filename},
            )
        except Exception as e:
            messages.error(request, f"Hiba: {str(e)}")
            return HttpResponseRedirect(request.path)

    return render(request, "admin_panel/upload.html")

def export_csv(request):
    excel_path = os.path.join(settings.BASE_DIR, "exported", "processed_data.xlsx")
    if os.path.exists(excel_path):
        return FileResponse(
            open(excel_path, "rb"),
            as_attachment=True,
            filename="feldolgozott_adatok.xlsx",
        )
    else:
        messages.error(request, "Nincs elérhető exportált fájl.")
        return HttpResponseRedirect(reverse("home"))


def export_excel(request):
    filename = request.GET.get("filename")
    filepath = os.path.join(settings.EXPORTED_DIR, filename)
    if os.path.exists(filepath):
        return FileResponse(open(filepath, "rb"), as_attachment=True, filename=filename)
    else:
        messages.error(request, "A fájl nem található.")
        return redirect("home")


def generate_height_chart(df):
    if df.empty:
        print("❌ Üres DataFrame, nincs mit megjeleníteni.")
        return None

    df = df.dropna(subset=["név", "testmagasság", "vttm"])

    if df.empty:
        print("❌ Nincs érvényes adat a diagramhoz.")
        return None

    import numpy as np

    names = df["név"].astype(str)
    current_heights = df["testmagasság"]
    expected_heights = df["vttm"]

    x = np.arange(len(names))

    plt.figure(figsize=(12, 6))

    bar_width = 0.35
    plt.bar(
        x - bar_width / 2, current_heights, width=bar_width, label="Jelenlegi magasság"
    )
    plt.bar(
        x + bar_width / 2,
        expected_heights,
        width=bar_width,
        alpha=0.7,
        label="Várható magasság",
        color="orange",
    )

    y_min = min(current_heights.min(), expected_heights.min()) - 5
    y_max = max(current_heights.max(), expected_heights.max()) + 5
    plt.ylim(y_min, y_max)

    plt.xticks(x, names, rotation=45, ha="right")
    plt.xlabel("Személy")
    plt.ylabel("Magasság (cm)")
    plt.title("Jelenlegi és várható testmagasság")
    plt.legend()
    plt.tight_layout()

    filename = f"chart_{int(time.time())}.png"
    chart_path = os.path.join(settings.MEDIA_ROOT, filename)
    plt.savefig(chart_path)
    return os.path.join(settings.MEDIA_URL, filename)


def calculate_plx(akk, kzk, vas):
    return akk + kzk + vas


def calculate_mk(ttm_kor, tts_kor, plx_kor, dck, diff):
    mk_base = 0.25 * (ttm_kor + tts_kor + plx_kor + dck)
    if diff < -1.99:
        correction = 1.08
    elif diff < -0.99:
        correction = 1.05
    elif diff > 1.99:
        correction = 0.92
    elif diff > 0.99:
        correction = 0.95
    else:
        correction = 1
    return mk_base * correction


def calculate_vttm(height, dck, gender):
    gender_str = str(gender).strip().lower()
    if gender_str == "f":
        return height + (18 - dck) * 0.5
    else:
        return height + (18 - dck) * 0.6


def download_template(request):
    template_path = os.path.join(settings.BASE_DIR, "static", "template.xlsx")
    if os.path.exists(template_path):
        return FileResponse(
            open(template_path, "rb"), as_attachment=True, filename="minta_adatlap.xlsx"
        )
    else:
        messages.error(request, "A sablon fájl nem található.")
        return redirect("home")
