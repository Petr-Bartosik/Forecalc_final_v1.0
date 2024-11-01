import pandas as pd
from decimal import Decimal
import os


def najdi_objem(delka, prumer):
    # Cesta k Excel souboru (upravte podle skutečné cesty)
    cesta_k_souboru = os.path.join(os.path.dirname(__file__), 'templates', 'evidence', 'objemova_tabulka.xlsx')

    print(f"Path to Excel: {cesta_k_souboru}")  # Výpis cesty pro kontrolu

    if not os.path.exists(cesta_k_souboru):
        print("Soubor nebyl nalezen.")
        return None

    # Načtení dat z Excelu bez použití prvního řádku jako hlavičky
    try:
        df = pd.read_excel(cesta_k_souboru, engine='openpyxl', header=None)
        print("Data úspěšně načtena z Excelu.")
    except Exception as e:
        print(f"Chyba při načítání souboru: {e}")
        return None

    # Výpis prvních několika řádků pro kontrolu
    print(df.head())

    # Ověření, zda tabulka obsahuje požadované hodnoty délky a průměru
    try:
        # Najít řádek odpovídající průměru (v prvním sloupci)
        radek = df[df.iloc[:, 0] == prumer]

        if not radek.empty:
            # Najít index sloupce odpovídající délce (v prvním řádku)
            sloupec_index = df.iloc[0, :].tolist().index(delka)

            # Získat hodnotu objemu na průsečíku
            objem = radek.iloc[0, sloupec_index]
            print(f"Nalezen objem: {objem}")
            return Decimal(objem)
        else:
            print(f"Průměr {prumer} nebyl nalezen.")
            return None
    except Exception as e:
        print(f"Chyba při zpracování dat: {e}")
        return None
