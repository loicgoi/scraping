import os
import pandas as pd
from get_data.get_scraping_data import scrape_books
from process_data.process_scraping_data import process_scraping_data
from database.insert_data import create_db, insert_data

def run_scraping_pipeline(
    pages: int = 5,
    base_url: str = "http://books.toscrape.com/catalogue/page-{}.html"
) -> pd.DataFrame:
    """
    Pipeline complet de scraping, nettoyage et insertion des données de livres.

    Étapes :
    1. Scraping des données sur plusieurs pages
    2. Sauvegarde des données brutes dans `data/data_scraping.csv`
    3. Nettoyage et conversion des types
    4. Insertion des données dans une base SQLite
    5. Affichage du nombre de livres insérés

    Args:
        pages (int, optional): Nombre de pages à scraper. Par défaut 5.
        base_url (str, optional): URL avec placeholder `{}` pour le numéro de page.
                                  Par défaut : "http://books.toscrape.com/catalogue/page-{}.html"

    Returns:
        pd.DataFrame: DataFrame final nettoyé et prêt à être utilisé.

    Exemple:
        >>> df = run_scraping_pipeline(pages=3)
        Étape 1 : Scraping des données...
        Étape 2 : Sauvegarde des données brutes...
        Étape 3 : Nettoyage des données...
        Étape 4 : Création et insertion en base...
        Nombre de livres insérés en base : 1000
        Pipeline terminé avec succès.
    """

    # Scraping des données
    print("Étape 1 : Scraping des données...")
    df_raw = scrape_books(pages, base_url)

    # Sauvegarde des données brutes
    print("Étape 2 : Sauvegarde des données brutes...")
    os.makedirs("data", exist_ok=True)
    df_raw.to_csv("data/data_scraping.csv", index=True)

    # Nettoyage des données
    print("Étape 3 : Nettoyage des données...")
    df_clean = process_scraping_data(df_raw)

    # Création et insertion en base
    print("Étape 4 : Création et insertion en base...")
    conn = create_db(df_clean)
    insert_data(conn)
    conn.close()

    print("Pipeline terminé avec succès.")
    return df_clean