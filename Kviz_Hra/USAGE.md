# Kviz Hra - Průvodce Obsluhou

Tento dokument je určen pro osoby, které budou aplikaci provozovat během soutěže.

## Příprava na Soutěž

### 1. Příprava Otázek

Před soutěží musíte připravit otázky a obrázky:

1. **Vyberte obrázky:**
   - Osobnosti (Alan Turing, Steve Jobs, ...)
   - Loga firem (Apple, Microsoft, Google, ...)
   - Technologické artefakty (starý počítač, iPhone, ...)
   - Screenshoty (Windows, Linux, ...)

2. **Upravte otázky:** Editujte `assets/questions.json`
   ```bash
   {
     "id": "q001",
     "title": "Jméno či popis",
     "image": "alan_turing.jpg",
     "answer": "Alan Turing",
     "category": "IT_Osobnosti",
     "difficulty": 2
   }
   ```

3. **Vložte obrázky:** Zkopírujte soubory do `assets/images/`
   ```
   assets/images/
   ├── alan_turing.jpg
   ├── steve_jobs.jpg
   ├── apple_logo.jpg
   └── ...
   ```

### 2. Testování Otázek

Spusťte aplikaci a otestujte každou otázku:

```bash
python main.py
```

- Zjistěte, zda se obrázek správně načítá
- Zkontrolujte správnost odpovědi
- Ověřte, že algoritm pixelace funguje korektně

### 3. Úprava Parametrů Hry

Pokud chcete změnit nastavení, editujte `config.py`:

```python
# Čas na řešení (v sekundách)
GAME_DURATION = 600  # 10 minut

# Startovní body
STARTING_POINTS = 120

# Velikost mřížky
GRID_SIZE = 4

# Penalizace za chybu
WRONG_ANSWER_COST = -20
```

## Spuštění Během Soutěže

### 1. Spuštění Aplikace

```bash
cd Kviz_Hra
python main.py
```

### 2. Výběr Otázky

1. Aplikace zobrazí seznam otázek
2. Vyberte správnou otázku (kliknutí v seznamu)
3. Klikněte "Spustit Hru"

### 3. Průběh Hry

**Obrazovka ukazuje:**
- ⏱️ **Zbývající čas** (nahoře vpravo)
- 💰 **Aktuální body** (nahoře vlevo)
- 🎨 **Skrytý obrázek** v 4×4 mřížce
- 📝 **Nápověda s blanky** (např. "A______ T______")

**Hráč může:**
- **Klikat na buňky** → Odkrýt část obrázku
- **Stisknout "Nápověda"** → Odhalí jedno písmeno
- **Napsat odpověď** → Do textového pole a Enter nebo tlačítko

### 4. Skončení Hry

Hra skončí když:
- ✅ Hráč zadá správnou odpověď
- ⏰ Čas vypršel
- 🛑 Hráč kliká "Skončit"

Aplikace zobrazí finální skóre.

## Správa Výsledků

### Ukládání Výsledků

Výsledky se automaticky ukládají do `results/` jako JSON soubory:

```
results/
├── result_20250324_103000.json
├── result_20250324_103145.json
└── ...
```

Každý soubor obsahuje:
- Otázku a odpověď
- Čas řešení
- Finální skóre
- Postupnost akcí

### Export Výsledků

Pro import do Excelu/Google Sheets:

```python
# Spusťte v Pythonu
import json
import csv

# Přečtěte JSON výsledky
with open('results/result_20250324_103000.json') as f:
    data = json.load(f)

# Exportujte CSV
with open('results.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['question_id', 'final_points', 'correct', 'elapsed_time'])
    writer.writerow({'question_id': data['question_id'], 'final_points': data['current_points'], ...})
```

## Tijmy a Více Účastníků

Pro soutěž více týmů v řadě:

1. Spusťte `python main.py`
2. Vyberte STEJNOU otázku pro všechny
3. Každý tým hraje postupně
4. Výsledky se ukládají samostatně

## Řešení Problémů

### Problém: Obrázek se nenačítá

**Řešení:**
- Zkontrolujte, že soubor existuje v `assets/images/`
- Ověřte, že jméno se shoduje v `questions.json` (bez `assets/images/`)
- Zkuste obrázek v jiném formátu (JPG, PNG)

### Problém: Aplikace se nespustí

**Řešení:**
```bash
# Instalujte Python 3.8+
python --version

# Instalujte závislosti
pip install -r requirements.txt

# Instalujte Tkinter
# Linux: sudo apt-get install python3-tk
# macOS: brew install python3-tk
```

### Problém: JSON chyba

**Řešení:**
- Otevřete `assets/questions.json` v textovém editoru
- Ověřte, že jsou všechny čárkam správně
- Počet `{` se musí rovnat počtu `}`
- Vyzkoušejte na [jsonlint.com](https://jsonlint.com/)

### Problém: Špatné bodování

**Řešení:**
- Zkontrolujte `config.py` nastavení
- Zajistěte, že `FIRST_CELL_COST = 0`
- Skóre se zobrazuje v levém horním rohu

## Bezpečnost a Ochrana Odpovědí

Aplikace chrání odpovědi následujícím způsobem:

✅ **Odpovědi nejsou viditelné v UI** - jen jako blanky (______)
✅ **Odpovědi jsou v externích souborech** - `questions.json`
✅ **Neexistuje dev console** - Tkinter není webová aplikace
✅ **Odpovědi se ověřují na pozadí** - Hráč nevidí backend kód

**Doporučení:**
- Nechte počítač s aplikací pod dohledem
- Zablokujte Alt+Tab během soutěže (pokud je potřeba)
- Neotevírejte `questions.json` během hry na viditelné obrazovce

## Čisti a Příprava na Příští Soutěž

### Zálohování Výsledků

Před smazáním app zkopírujte `results/`:
```bash
# Vytvořte zálohu
xcopy results results_backup /E /I
```

### Vymazání Starých Výsledků

```bash
# Smažte results/ a znovu je vytvořte
rmdir /S results
mkdir results
```

## Kontakt na Podporu

Při technických problémech během soutěže:
1. Zkontrolujte README.md sekcí Troubleshooting
2. Restartujte aplikaci
3. Přepněte na jiný počítač (pokud je k dispozici)

---

**Poznámka:** Tato aplikace je určena pro učitele a správce soutěže. Hráči by měli mít jasné pokyny, jak ji používat.
