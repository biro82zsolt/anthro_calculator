
# 🧮 Antropometriai Kalkulátor – Vizsgaprojekt

Ez az alkalmazás egy oktatási célú antropometriai kalkulátor, amely lehetővé teszi a gyermekek morfológiai korának (MK), testarányainak (PLX), valamint várható testmagasságának (VTTM) becslését mért adatok alapján.

## 🎯 Funkciók

- ✅ CSV vagy Excel alapú adatfeltöltés
- ✅ Morfológiai kor, PLX és VTTM automatikus számítása
- ✅ Jelenlegi és várható testmagasság vizualizálása diagramon
- ✅ Eredmények letölthetők Excel formátumban
- ✅ Demó mód beépített mintaadattal
- ✅ Sötét/világos mód váltási lehetőség
- ✅ Jupyter Notebook adatelemzéssel
- ✅ Egységtesztelés és Black kódformázás

## 🚀 Használat

### 1. Telepítés

```bash
git clone https://github.com/<sajat-repo>/anthropometric-calculator.git
cd anthropometric-calculator
pip install -r requirements.txt
```

### 2. Futtatás

```bash
python manage.py runserver
```

Ezután látogasd meg: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 📂 Mappastruktúra

```
project_root/
├── admin_panel/         # Feltöltés, diagram megjelenítés
├── anthro_app/          # Számítások (MK, PLX, VTTM)
├── landing/             # Főoldal, demó, sablon letöltés
├── static/              # Statikus fájlok (logó, chart, sablon)
├── exported/            # Ide kerülnek a generált Excel fájlok
├── templates/           # HTML sablonok
├── tests/               # Egységtesztek
├── jupyter_notebook.ipynb
└── requirements.txt
```

## 🧪 Tesztelés

Futtatás:

```bash
python -m unittest discover tests
```

## 📈 Jupyter Notebook

A `jupyter_notebook.ipynb` fájl példákat tartalmaz a számításokra, adatvizualizációra és MK/VTTM értelmezésre.

## 📋 CSV sablon

Letölthető a főoldalról mintafájl, amit `.csv` formátumban kell menteni:

- **Elválasztó:** pontosvessző `;`
- **Kódolás:** UTF-8

---

## 🧠 Jövőbeli fejlesztések

- 🔒 Bejelentkezés & adminfelület
- 📊 Egyéni statisztikák
- 🌍 Többnyelvű támogatás
- ☁️ Felhő alapú tárolás

---

Készítette: *[Saját neved]* – 2025  
Középhaladó Python/Django vizsgafeladat
