import sys
import os

# Menambahkan folder 'backend' ke path Python agar import 'app.xxx' tetap jalan
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "backend"))

from app.main import app
