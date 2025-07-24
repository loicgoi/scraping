import pandas as pd
import os
from get_data.get_api_data import search_books
from process_data.process_api_data import process_api_data
from database.insert_data import create_db, insert_data

def run_api_pipeline(
    query: str = "food",
    max_results: int = 40
) -> None:
    """
    Pipeline complet :
    1. Requête Google Books
    2. Sauvegarde CSV brute
    3. Nettoyage
    4. Insertion SQLite
    """

    # Requête Google Books
    print("Requête Google Books...")
    raw = search_books({"q": query, "maxResults": max_results, "filter": "paid-ebooks"})

    # Sauvegarde des données brutes
    print("Sauvegarde CSV brute...")
    os.makedirs("data", exist_ok=True)
    pd.json_normalize(raw.get("items", [])).to_csv("data/data_api_raw.csv", index=True)

    # Nettoyage des données
    print("Nettoyage des données...")
    df_clean = process_api_data(raw)
    df_clean.to_csv("data/data_api.csv", index_label="index")

    # Insertion en base de données SQLite
    print("Insertion en base SQLite...")
    conn = create_db(df_clean)
    insert_data(conn)
    conn.close()

    print("Pipeline API terminé.")