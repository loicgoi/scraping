import pandas as pd
import os
from get_data.get_api_data import search_books
from process_data.process_api_data import process_api_data
from database.insert_data import create_db, insert_data

def run_api_pipeline(
    query: str = "food",
    max_results: int = 40,
    min_rating: int = 1  # ajout du rating minimal
) -> None:
    """
    Pipeline complet :
    1. Requête Google Books avec pagination et filtrage sur rating
    2. Sauvegarde CSV brute
    3. Nettoyage
    4. Insertion SQLite
    """

    print("Requête Google Books...")
    raw_books = search_books(

        params={
            "q": query, 
            "filter": "paid-ebooks", 
            "maxResults": 40,
        },
        min_rating=min_rating,
        desired_results=max_results,
        query=query
    )

    # On récupère une liste filtrée, on crée donc un dict 'fausse API' pour garder la structure actuelle
    raw = {"items": raw_books}

    print("Sauvegarde CSV brute...")
    os.makedirs("data", exist_ok=True)
    pd.json_normalize(raw.get("items", [])).to_csv("data/data_api_raw.csv", index=True)

    print("Nettoyage des données...")
    df_clean = process_api_data(raw)
    df_clean.to_csv("data/data_api.csv", index_label="index")

    print("Insertion en base SQLite...")
    conn = create_db(df_clean)
    insert_data(conn)
    conn.close()

    print("Pipeline API terminé.")
