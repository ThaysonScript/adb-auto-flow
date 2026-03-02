import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEVICE_ID = os.getenv("DEVICE_ID") or None
    APP_PACKAGE = os.getenv("TARGET_APP_PACKAGE")
    SEARCH_URL = os.getenv("TARGET_SEARCH_URL")
    
    MIN_DELAY = float(os.getenv("MIN_DELAY", 3.5))
    MAX_DELAY = float(os.getenv("MAX_DELAY", 9.0))
    MISCLICK_CHANCE = float(os.getenv("CHANCE_OF_MISCLICK", 0.15))
    
    # Adicionado os campos que faltavam
    SCROLL_MIN = int(os.getenv("SCROLL_SPEED_MIN", 400))
    SCROLL_MAX = int(os.getenv("SCROLL_SPEED_MAX", 1200))
    
    WIDTH = int(os.getenv("SCREEN_WIDTH", 1080))
    HEIGHT = int(os.getenv("SCREEN_HEIGHT", 2400))
    SEARCH_TERMS_FILE = os.getenv("SEARCH_TERMS_FILE", "data/search_terms.txt")

cfg = Config()