import pandas as pd


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
    try:
        gender_str = str(gender).strip().lower()
        if gender_str == "f":
            return height + (18 - dck) * 0.5
        else:
            return height + (18 - dck) * 0.6
    except Exception as e:
        print(f"VTTM számítási hiba: {e}")
        return None


def process_dataframe(df):
    if "VTTM" in df.columns:
        df.drop(columns=["VTTM"], inplace=True)

    df = df.copy()

    df.columns = df.columns.str.strip().str.lower()
    df["testmagasság"] = pd.to_numeric(df["testmagasság"], errors="coerce")
    df["neme"] = df["neme"].astype(str).str.strip().str.lower()

    # PLX számítás
    df["plx"] = df["akk"] + df["kzk"] + df["vas"]

    # DCK
    df["dck"] = (
        pd.to_datetime(df["mérés_dátuma"], format="mixed", dayfirst=False)
        - pd.to_datetime(df["születési_dátum"], format="mixed", errors="raise")
    ).dt.days / 365.25

    # Dummy referenciaértékek
    df["ttm_kor"] = df["dck"]
    df["tts_kor"] = df["dck"]
    df["plx_kor"] = df["dck"]
    df["eltérés"] = df["ttm_kor"] - df["dck"]

    df["mk"] = df.apply(
        lambda row: calculate_mk(
            row["ttm_kor"], row["tts_kor"], row["plx_kor"], row["dck"], row["eltérés"]
        ),
        axis=1,
    )

    df["vttm"] = df.apply(
        lambda row: calculate_vttm(row["testmagasság"], row["dck"], row["neme"]), axis=1
    )

    df = df.dropna(subset=["testmagasság", "vttm"])

    return df
