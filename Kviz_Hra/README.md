# Kviz Hra - Interaktivní Soutěžní Aplikace

Aplikace pro interaktivní znalostní soutěž základních škol s odhalováním obrázku a tajenkou.

## Charakteristiky

- **4×4 Mřížka**: Skrytý obrázek rozdělený na 16 buněk
- **Bodový Systém**: Prvních buněk zdarma, pak -1, -2, -3... bodů
- **Nápovědy**: Postupné odkrývání písmen s bodovou penalizací
- **Časový Limit**: 10 minut na vyřešení
- **Ochrana Odpovědí**: Odpovědi uloženy v externích souborech
- **Výsledky**: Automatické ukládání skóre a průběhu hry

## Instalace

### Požadavky
- Python 3.8+
- Tkinter (obvykle součást Pythonu)

### Postup

1. Nainstalujte závislosti:
```bash
pip install -r requirements.txt
```

2. Vytvořte adresář `assets/images/` a vložte své obrázky:
```
assets/
└── images/
    └── your_image.jpg
```

3. Upravte `assets/questions.json` se svými otázkami (viz níže)

## Spuštění

```bash
python main.py
```

## Formát questions.json

Soubor `assets/questions.json` obsahuje seznam otázek:

```json
[
  {
    "id": "q001",
    "title": "Název otázky",
    "image": "filename.jpg",
    "answer": "Správná odpověď",
    "category": "Kategorie",
    "difficulty": 3,
    "description": "Popis otázky"
  }
]
```

## Struktura Projektu

```
Kviz_Hra/
├── main.py              # Vstupní bod aplikace
├── config.py            # Konfigurace hry
├── models.py            # Datové modely
├── game.py              # Herní logika
├── ui.py                # Uživatelské rozhraní
├── image_processor.py   # Zpracování obrázků
├── data_loader.py       # Načítání dat
├── requirements.txt     # Závislosti
├── assets/
│   ├── questions.json   # Otázky
│   └── images/          # Obrázky
└── results/             # Ukládané výsledky
```

## Herní Pravidla

### Bodový Systém

**Odkrývání Buněk:**
- 1. buňka: 0 bodů (zdarma)
- 2. buňka: -1 bod
- 3. buňka: -2 body
- n. buňka: -(n-1) bodů

**Nápovědy (Písmena):**
- 1. nápověda: -2 body
- 2. nápověda: -3 body
- n. nápověda: -(n+1) bodů

**Chybná Odpověď:** -20 bodů

### Časový Limit

- Hra trvá **10 minut** (600 sekund)
- Po vypršení času se hra automaticky ukončí
- Výsledky se uloží

### Startovní Body

- Každý hráč začíná s **120 body**
- Body nemohou jít pod 0
- Finální skóre = zbývající body

## Výstupní Data

Výsledky hry se ukládají do `results/` jako JSON:

```json
{
  "question_id": "q001",
  "start_time": "2025-03-24T10:30:00",
  "elapsed_time": 345,
  "current_points": 92,
  "revealed_cells": [0, 1, 2, ...],
  "letter_hints_used": 2,
  "attempts": [...],
  "game_over": true,
  "game_end_reason": "completed"
}
```

## Konfigurace

Upravit lze v `config.py`:

```python
GAME_DURATION = 600      # Čas v sekundách (10 minut)
STARTING_POINTS = 120    # Startovní body
GRID_SIZE = 4            # Velikost mřížky (4x4)
CELL_SIZE = 60           # Velikost buňky v pixelech
```

## Přidávání Vlastních Otázek

1. Vložte svůj obrázek do `assets/images/`
2. Otevřete `assets/questions.json`
3. Přidejte novou otázku:

```json
{
  "id": "q006",
  "title": "Moje otázka",
  "image": "muj_obrazek.jpg",
  "answer": "Správná odpověď",
  "category": "Moje_Kategorie",
  "difficulty": 2
}
```

4. Uložte a spusťte `python main.py`

## Odstraňování Problémů

**Chyba "Image not found":**
- Ověřte, že soubor obrázku existuje v `assets/images/`
- Ověřte správné jméno v `questions.json`

**Chyba "JSONDecodeError":**
- Ověřte, že `assets/questions.json` je validní JSON
- Použijte [jsonlint.com](https://jsonlint.com/) k ověření

**Tkinter není dostupný:**
```bash
# Linux (Debian/Ubuntu)
sudo apt-get install python3-tk

# macOS
brew install python3-tk

# Windows - Instalujte Python s Tkinter

```

## Vývoj a Rozšíření

### Přidání nového stylu/tématu
Upravte barvy v `config.py`:
```python
COLOR_HIDDEN = "#444444"
COLOR_REVEALED = "#CCCCCC"
```

### Přidání více funkcí
- Více variant otázek
- Týmový mód
- Leaderboard
- Statistiky

## Licence

Školní projekt - Čtvrtletní projekt z programování v Pythonu

## Autor

Vytvořeno jako součást školního projektu.

## Podpora

Při problémech:
1. Ověřte, že všechny závislosti jsou nainstalovány
2. Zkontrolujte `assets/questions.json`
3. Ujistěte se, že Python 3.8+ je nainstalován
4. Zkuste spustit z příkazového řádku pro více informací o chybách
