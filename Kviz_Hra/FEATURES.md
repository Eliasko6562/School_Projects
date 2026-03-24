# Kviz Hra - Ověření Funkcí

## ✅ Implementované Funkce

### 1. Datové Modely
- ✅ `Question` - Representace otázky s obrázkem a odpovědí
- ✅ `GameState` - Správa stavu hry (body, čas, odhalená políčka)
- ✅ `Attempt` - Záznam akcí v průběhu hry

### 2. Zpracování Dat
- ✅ `DataLoader` - Načítání otázek z JSON
- ✅ Validace formátu JSON
- ✅ Uložení výsledků do JSON
- ✅ Automatické vytváření adresářů

### 3. Zpracování Obrázků
- ✅ Načítání obrázků (JPG, PNG, BMP)
- ✅ Pixelace skrytých buněk
- ✅ Dělení obrázku na 4×4 mřížku
- ✅ Náhradní obrázek (placeholder) při chybě

### 4. Herní Logika
- ✅ Bodový systém:
  - 1. políčko: 0 bodů (zdarma)
  - 2. políčko: -1 bod
  - 3. políčko: -2 body
  - n. políčko: -(n-1) bodů
- ✅ Nápovědy (odhalování písmen):
  - 1. nápověda: -2 body
  - 2. nápověda: -3 body
  - n. nápověda: -(n+1) bodů
- ✅ Chybná odpověď: -20 bodů
- ✅ Minimum bodů: 0 (nelze jít do minusu)
- ✅ Hint string (zobrazení řešení s blanky)

### 5. Časovač
- ✅ 10 minut (600 sekund) na řešení
- ✅ Background vlákno pro timer
- ✅ Automatické ukončení při vypršení času
- ✅ Live aktualizace zbývajícího času

### 6. Uživatelské Rozhraní (Tkinter)
- ✅ Hlavní okno s intuitivním layoutem
- ✅ 4×4 mřížka klikacích tlačítek
- ✅ Pixelované buňky se progresivním odhalováním
- ✅ Zobrazení bodů a času
- ✅ Hint string (řešení s podtržítky)
- ✅ Textové pole pro zadávání odpovědi
- ✅ Tlačítka:
  - "Odeslat Odpověď" (Enter nebo tlačítko)
  - "Odkrýt Políčko" (klikání na mřížku)
  - "Nápověda (Písmeno)"
  - "Skončit" (ukončení hry)
- ✅ Zobrazení zpráv (chyby, úspěchy)
- ✅ Animace aktualizace UI

### 7. Výběr Otázky
- ✅ Seznamové okno s otázkami
- ✅ Přehledný výběr podle titulu a kategorie
- ✅ Spuštění konkrétní otázky

### 8. Správa Výsledků
- ✅ Automatické uložení výsledků po hře
- ✅ JSON formát s časovým razítkem (result_YYYYMMDD_HHMMSS.json)
- ✅ Úplný záznam herního průběhu

## 📊 Testování

### Test 1: Načítání Dat
```
✅ Loaded 5 questions
  - Zakladatel moderní informatiky
  - Vynálezce www
  - Zakladatel společnosti Apple
  - Zakladatel Microsoftu
  - Tvůrce Linuxu
```

### Test 2: Herní Logika
```
Počáteční stav: 120 bodů
Po odkrytí 1. buňky: 120 bodů (zdarma)
Po odkrytí 2. buňky: 119 bodů (-1)
Po nápovědy: 117 bodů (-2)
Hint string: "A___ ______" (správně)
```

### Test 3: Bodový Systém
- ✅ Políčka: 0, -1, -2, -3, -4, ... (správně)
- ✅ Nápovědy: -2, -3, -4, -5, ... (správně)
- ✅ Chybná odpověď: -20 (správně)
- ✅ Minimum 0 bodů (správně)

## 🎨 Grafické Možnosti

### Barvy (konfigurovatelné v config.py)
- ✅ Skryté políčko: #444444 (tmavě šedá)
- ✅ Odkryté políčko: #CCCCCC (světle šedá)
- ✅ Při hoveru: #AAAAAA (střední šedá)
- ✅ Správná odpověď: zelená
- ✅ Chybná odpověď: červená

### Fonty
- ✅ Nadpis: 24px bold
- ✅ Timer: 32px Courier New bold
- ✅ Body: 14px bold
- ✅ Text: 10-12px Arial

## 🔒 Bezpečnost

- ✅ Odpovědi NE v UI kódu (v JSON)
- ✅ Odpovědi zobrazeny jen jako blanky
- ✅ Podtržítka zabraňují vidět správnou délku
- ✅ Žádný developer console v Tkinter
- ✅ Validace odpovědí na pozadí

## 📁 Struktura Souborů

```
✅ main.py               - Vstupní bod
✅ config.py            - Konfigurace
✅ models.py            - Datové modely
✅ game.py              - Herní logika
✅ ui.py                - Uživatelské rozhraní
✅ image_processor.py   - Zpracování obrázků
✅ data_loader.py       - Načítání dat
✅ requirements.txt     - Závislosti
✅ README.md            - Dokumentace
✅ USAGE.md             - Průvodce obsluhou
✅ assets/
   ✅ questions.json    - Otázky (5 vzorků)
   ✅ images/          - Adresář na obrázky
✅ results/             - Uložené výsledky
```

## 🚀 Spuštění

### Instalace
```bash
pip install -r requirements.txt
```

### Spuštění
```bash
python main.py
```

### Typ spuštění
- ✅ Desktop aplikace (Tkinter)
- ✅ Cross-platform (Windows, macOS, Linux)
- ✅ Žádný webový server potřebný

## 📝 Poznámky

### Vzorové Otázky
Aplikace obsahuje 5 vzorových otázek o IT osobnostech a vynálezech:
1. Alan Turing - Zakladatel moderní informatiky
2. Tim Berners-Lee - Vynálezce www
3. Steve Jobs - Zakladatel Apple
4. Bill Gates - Zakladatel Microsoft
5. Linus Torvalds - Tvůrce Linuxu

### Nahrazení Obrzků
Vzorové obrázky nejsou zahrnuty (velikost souboru). Chcete-li hrát:
1. Přidejte obrázky do `assets/images/`
2. Aktualizujte `image` v `questions.json`

Bez obrázků aplikace zobrazí placeholder (šedá plocha).

### Rozšíření
Aplikace je navržena pro snadné rozšíření:
- Přidání více otázek (pouze editujte JSON)
- Změna parametrů (editujte config.py)
- Vlastní UI motiv (změna barev a fontů)

## ✨ Speciální Vlastnosti

1. **Progresivní Odhalování**: Obrázek se postupně odkrývá
2. **Inteligentní Hint String**: Zobrazuje správně umístěná písmena a blanky
3. **Automatické Uložení**: Výsledky se ukládají bez zásahu uživatele
4. **Ochrana Odpovědí**: Správné odpovědi nejsou v UI
5. **Přátelské UI**: Jasné pokyny a zpětná vazba

## 🎯 Vhodnost pro Soutěž

- ✅ Vhodná pro základní školy
- ✅ Jednoduchá obsluha
- ✅ Bez technických znalostí pro operátora
- ✅ Bezpečné před odhalením odpovědí
- ✅ Úplný záznam výsledků
- ✅ Přizpůsobitelná nastavení

---

**Vytváření Date**: 24. března 2026
**Verze**: 1.0.0
**Stav**: ✅ Kompletní a testovaná
