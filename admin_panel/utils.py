import os
import pandas as pd
from django.conf import settings


def export_dataframe_to_excel(df):
    export_dir = os.path.join(settings.BASE_DIR, "exported")
    os.makedirs(export_dir, exist_ok=True)

    export_columns = ["név", "születési_dátum", "mérés_dátuma", "testmagasság", "vttm"]

    df_export = df.copy()

    # Csak a szükséges oszlopokat tartalmazza
    df_export = df_export[export_columns]

    export_path = os.path.join(export_dir, "processed_data.xlsx")
    df_export.to_excel(export_path, index=False)

    return export_path
