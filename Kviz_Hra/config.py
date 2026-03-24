"""
Configuration settings for Kviz_Hra application
"""

import os

# ============================================
# HERNÍ PARAMETRY / GAME PARAMETERS
# ============================================

GAME_DURATION = 600  # sekund (10 minut)
STARTING_POINTS = 120
MAX_SAFE_POINTS = 120

# ============================================
# BODOVÝ SYSTÉM / SCORING SYSTEM
# ============================================

# Odhalování políček / Cell revelation
FIRST_CELL_COST = 0
CELL_COST_INCREMENT = 1  # n-tém políčku stojí -(n-1)

# Nápovědy na písmena / Letter hints
FIRST_LETTER_HINT_COST = -2
LETTER_HINT_COST_INCREMENT = 1  # n-té nápovědy stojí -(n+1)

# Chybné odpovědi / Wrong answers
WRONG_ANSWER_COST = -20
MINIMUM_POINTS = 0  # Body nemohou jít pod 0

# ============================================
# UI NASTAVENÍ / UI SETTINGS
# ============================================

# Mřížka obrázku / Image grid
GRID_SIZE = 4  # 4x4
CELL_SIZE = 60  # pixely na buňku
IMAGE_SIZE = (240, 240)  # GRID_SIZE * CELL_SIZE

# Barvy / Colors
COLOR_HIDDEN = "#444444"
COLOR_REVEALED = "#CCCCCC"
COLOR_HOVER = "#AAAAAA"
COLOR_TEXT = "#000000"
COLOR_CORRECT = "#00AA00"
COLOR_WRONG = "#AA0000"
COLOR_INFO_BG = "#FFFFFF"
COLOR_INFO_FG = "#000000"

# Font
FONT_MAIN = ("Arial", 10)
FONT_TIMER = ("Courier New", 32, "bold")
FONT_POINTS = ("Arial", 14, "bold")
FONT_LABEL = ("Arial", 11)
FONT_ANSWER_INPUT = ("Arial", 12)

# Okno / Window
WINDOW_TITLE = "Kviz Hra - Znalostní Soutěž"
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 700

# ============================================
# CESTY A SOUBORY / PATHS AND FILES
# ============================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

QUESTIONS_FILE = os.path.join(BASE_DIR, "assets", "questions.json")
RESULTS_DIR = os.path.join(BASE_DIR, "results")
IMAGES_DIR = os.path.join(BASE_DIR, "images")

# Pokud adresář na výsledky neexistuje, vytvoř ho
os.makedirs(RESULTS_DIR, exist_ok=True)
os.makedirs(IMAGES_DIR, exist_ok=True)

# ============================================
# POKROČILÉ NASTAVENÍ / ADVANCED SETTINGS
# ============================================

# Bezpečnost / Security
VALIDATE_ANSWERS = True
CHECK_INTEGRITY = False

# Logging
DEBUG_MODE = False
LOG_FILE = os.path.join(BASE_DIR, "debug.log")

# Performance
CACHE_IMAGES = True
PRELOAD_QUESTIONS = True

# ============================================
# Textové konstanty / TEXT CONSTANTS
# ============================================

GAME_TITLE = "KVIZ HRA"
GAME_SUBTITLE = "Znalostní Soutěž"

TEXT_SCORE = "Body:"
TEXT_TIME = "Čas:"
TEXT_TIME_REMAINING = "Zbývající čas:"
TEXT_ENTER_ANSWER = "Zadejte řešení:"
TEXT_SUBMIT_ANSWER = "Odeslat Odpověď"
TEXT_REVEAL_CELL = "Odkrýt Políčko"
TEXT_LETTER_HINT = "Nápověda (Písmeno)"
TEXT_QUIT_GAME = "Skončit"
TEXT_GAME_OVER_TIME = "Čas vypršel!"
TEXT_CORRECT = "✓ Správně!"
TEXT_WRONG = "✗ Chybně! -20 bodů"
TEXT_ALREADY_REVEALED = "Toto políčko je již odkryté!"
TEXT_TIME_EXPIRED = "Čas vypršel. Hra skončila."
