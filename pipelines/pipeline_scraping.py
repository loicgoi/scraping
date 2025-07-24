import pandas as pd
from get_data.get_scraping_data import get_books_html
from process_data.process_scraping_data import parse_books_html, process_scraping_data
from database.insert_data import insert_data, create_db

import pandas as pd
from get_data.get_scraping_data import get_books_html
from process_data.process_scraping_data import parse_books_html, process_scraping_data
from database.insert_data import insert_data, create_db

def run_scraping_pipeline(
    pages: int = 5,
    base_url: str = "http://books.toscrape.com/catalogue/page-{}.html"
) -> pd.DataFrame:
    """
    Exécute les fonctions pour extraire les données du site sur plusieurs pages,
    les traiter et les insérer dans la base de données.

    Args:
        pages (int): Nombre de pages à scraper (par défaut 5).
        base_url (str): URL avec {} pour numéro de page (modifiable).

    Returns:
        pd.DataFrame: Un DataFrame contenant les données extraites du site.
    """

    df_list = []

    print("Étape 1 : Récupération du HTML sur plusieurs pages...")
    for page_num in range(1, pages + 1):
        url = base_url.format(page_num)
        print(f" - Page {page_num} : {url}")
        soup = get_books_html(url)
        df_page = parse_books_html(soup)
        df_list.append(df_page)

    print("Étape 2 : Concatenation des données brutes...")
    df_books = pd.concat(df_list, ignore_index=True)

    # Enregistrement local des données brutes
    df_books.to_csv("data/books_infos.csv", index=False)

    print("Étape 3 : Nettoyage et conversion des types...")
    df_books = process_scraping_data(df_books)

    print("Étape 4 : Création de la base de données...")
    connection, df_books = create_db(df_books)

    print("Étape 5 : Insertion des données en base...")
    insert_data(connection, df_books)

    print("Pipeline terminée avec succès.")
    return df_books
