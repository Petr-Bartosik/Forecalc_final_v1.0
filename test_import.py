import sys
import os

# Přidání cesty k adresáři `forest`, kde je složka `drivi_app`
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from drivi_app.evidence.utils import najdi_objem

print("Import byl úspěšný.")
