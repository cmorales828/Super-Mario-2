import sys
import os

def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

GLOBAL_PATH = resource_path("assets/")
MAP_PATH = GLOBAL_PATH + "maps/"
TILE_SIZE = 16
ZOOM = 3
COLOR_MASK = (255, 0, 255)