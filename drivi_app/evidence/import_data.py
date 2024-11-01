import pandas as pd
from your_project.your_app.models import WoodVolume

# Načtení CSV souboru
df = pd.read_csv('cesta/k/updated_table.csv', header=None)

# Iterace přes DataFrame a ukládání dat do databáze
for index, row in df.iterrows():
    length = row[0]  # První sloupec obsahuje délku
    for col in range(1, len(row)):
        diameter = col
        volume = row[col]
        WoodVolume.objects.create(length=length, diameter=diameter, volume=volume)
