# Kviz Hra - Spustit Aplikaci za 1 Minutu

## 🚀 Rychlý Start

### 1. Instalace (prvně)
```bash
cd Kviz_Hra
pip install -r requirements.txt
```

### 2. Spuštění
```bash
python main.py
```

### 3. Vyberte otázku a klikněte "Spustit Hru"

---

## 📋 Kompletní Obsah Projektu

```
Kviz_Hra/
│
├── 🎮 SPUSTITELNÉ SOUBORY
│   └── main.py                     ← Spusťte tímto (python main.py)
│
├── ⚙️ KONFIGURACE & LOGIKA
│   ├── config.py                   - Všechna nastavení (čas, body, barvy)
│   ├── models.py                   - Datové třídy (Question, GameState, Attempt)
│   ├── game.py                     - Herní logika (bodování, timer)
│   ├── ui.py                       - Uživatelské rozhraní (Tkinter)
│   ├── image_processor.py          - Zpracování obrázků (pixelace, mřížka)
│   └── data_loader.py              - Čtení/zápis otázek a výsledků
│
├── 📚 DOKUMENTACE
│   ├── README.md                   - Komp. pokyny (instalace, pravidla, FAQ)
│   ├── USAGE.md                    - Průvodce obsluhou (pro operátory)
│   ├── FEATURES.md                 - Seznam všech implementovaných funkcí
│   └── QUICKSTART.md               - Tento soubor (rychlý start)
│
├── 📦 ZÁVISLOSTI
│   └── requirements.txt            - pip install -r requirements.txt
│
├── 📁 DATA
│   ├── assets/
│   │   ├── questions.json          - 5 vzorových otázek
│   │   └── images/                 - Sem vložit obrázky (.jpg, .png, ...)
│   └── results/                    - Automaticky uložené výsledky her
│
└── 📄 OSTATNÍ
    └── copilot_instruction.md      - Původní zadání projektu
```

---

## 🎯 Co Dělá Aplikace

**Kviz Hra** je interaktivní soutěžní aplikace pro základní školy:

1. **Skrytý obrázek** v 4×4 mřížce (16 buněk)
2. Hráč **klikací na buňky** a vidí části obrázku
3. **Progressivní cena**: 1. buňka grátis, 2. stojí -1 bod, 3. stojí -2 body, ...
4. Lze si vzít **nápovědu** (odhalí písmeno) za -2, -3, -4... bodů
5. **Chybná odpověď** stojí -20 bodů
6. **Časový limit**: 10 minut
7. **Automatické uložení** výsledků

---

## 💻 Systémové Požadavky

- **Python**: 3.8 nebo novější
- **OS**: Windows, macOS, Linux
- **Paměť**: 256 MB RAM
- **Disk**: 10 MB volného místa
- **Tkinter**: Obvykle součástí Pythonu

### Kontrola Instalace
```bash
python --version          # Musí být 3.8+
python -m tkinter         # GUI framework (měl by se otevřít malý test)
```

---

## 🎮 Jak Hrát

1. **Spusťte aplikaci**: `python main.py`
2. **Vyberte otázku** ze seznamu
3. **Klika na buňky** v 4×4 mřížce (obrázek se postupně odkrývá)
4. **(Volitelně)** Stiskněte "Nápověda (Písmeno)" pro odhalení písmene
5. **Zadejte odpověď** v textovém poli
6. Stiskněte **Enter** nebo tlačítko "Odeslat Odpověď"
7. Aplikace uloží vaš výsledek

---

## 📝 Přidání Vlastních Otázek

### Krok 1: Připravte Obrázek
```
assets/images/
└── vasObrazek.jpg      ← Jpeg, PNG, BMP, ...
```

### Krok 2: Editujte questions.json
Otevřete `assets/questions.json` a přidejte:

```json
{
  "id": "q006",
  "title": "Název otázky",
  "image": "vasObrazek.jpg",
  "answer": "Správná Odpověď",
  "category": "Kategorie",
  "difficulty": 2,
  "description": "Volitelný popis"
}
```

### Krok 3: Spusťte Aplikaci
```bash
python main.py
```

Vaše nová otázka se objeví v seznamu!

---

## 🔧 Úprava Nastavení

Editujte `config.py`:

```python
GAME_DURATION = 600      # Čas v sekundách (10 minut)
STARTING_POINTS = 120    # Startovní body
WRONG_ANSWER_COST = 20   # Penalizace za chybu
GRID_SIZE = 4            # Velikost mřížky (4x4)
```

Změny se projeví po restartu.

---

## ❌ Řešení Problémů

### Chyba: "Obrázek nenalezen"
```
✗ Řešení: Zkontrolujte, že je obrázek v assets/images/
         Zkontrolujte jméno v questions.json
```

### Chyba: "JSON chyba"
```
✗ Řešení: Otevřete assets/questions.json
         Zkontrolujte všechny čárky a závorky
         Vyzkoušejte https://jsonlint.com/
```

### Tkinter není dostupný
```bash
# Linux (Debian/Ubuntu)
sudo apt-get install python3-tk

# macOS
brew install python3-tk

# Windows
← Python si znovu nainstalujte, zaškrtněte Tkinter
```

### Aplikace se nespustí
```bash
python --version          # Musí být 3.8+
pip install -r requirements.txt  # Instalujte závislosti
python main.py            # Spusťte znovu
```

---

## 📊 Výsledky

Po každé hře se automaticky uloží výsledek:

```
results/
└── result_20250324_103000.json    ← Obsahuje všechny detaily hry
```

Obsah:
- ✅ Otázka a odpověď
- ✅ Skóre a čas
- ✅ Odkrytá políčka
- ✅ Všechny akce v pořadí

---

## 🎨 Přizpůsobení Vzhledu

Editujte barvy v `config.py`:

```python
COLOR_HIDDEN = "#444444"      # Skryté políčko
COLOR_REVEALED = "#CCCCCC"    # Odkryté políčko
COLOR_CORRECT = "#00AA00"     # Zelená (správně)
COLOR_WRONG = "#AA0000"       # Červená (chybně)
```

Fonty:
```python
FONT_TIMER = ("Courier New", 32, "bold")    # Timer
FONT_POINTS = ("Arial", 14, "bold")         # Body
```

---

## 🌟 Speciální Funkce

✅ **Bez cloudů** - Vše běží lokálně  
✅ **Bezpečné** - Odpovědi nejsou v UI  
✅ **Jednoduché** - Bez zbytečné složitosti  
✅ **Rozšiřitelné** - Snadno přidat otázky  
✅ **Offline** - Nepotřebuje Internet  

---

## 📞 Support

Máte problém? Zkontrolujte:
1. [README.md](README.md) - Detailní dokumentace
2. [USAGE.md](USAGE.md) - Průvodce obsluhou
3. [FEATURES.md](FEATURES.md) - Implementované funkce

---

## 🎓 Školní Projekt

Čtvrtletní projekt z Programování v Pythonu  
**Téma**: Interaktivní soutěžní aplikace pro znalostní soutěž  
**Autor**: Váš tým  
**Verze**: 1.0.0  
**Datum**: Březen 2025  

---

**🚀 Hotovo! Nyní si můžete zahrát: `python main.py`**
