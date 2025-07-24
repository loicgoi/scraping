import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_books(pages: int, base_url: str) -> pd.DataFrame:
    """
    Scrape les informations des livres sur plusieurs pages du site books.toscrape.com
    et retourne un DataFrame brut contenant les données extraites.

    Args:
        pages (int): Nombre de pages à scraper.
        base_url (str): URL de base avec un placeholder `{}` pour le numéro de page.
                        Exemple : "http://books.toscrape.com/catalogue/page-{}.html"

    Returns:
        pd.DataFrame: DataFrame contenant les colonnes suivantes :
            - title (str) : Titre du livre
            - price (str) : Prix brut avec symbole £
            - rating (str) : Note textuelle (ex: "Three")
            - availability (str) : Disponibilité brute (ex: "In stock")

    Raises:
        requests.exceptions.HTTPError: Si une requête échoue.
    """

    # Scraping des données sur plusieurs pages
    all_books = []

    for page_num in range(1, pages + 1):
        url = base_url.format(page_num)
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        # Extraction des données des livres
        books = soup.select("article.product_pod")
        for book in books:
            title = book.h3.a["title"]
            price = book.select_one("p.price_color").text.strip()
            rating = book.p["class"][1]
            availability = book.select_one("p.instock.availability").text.strip()
            
            # Ajout des données extraites au DataFrame
            all_books.append({
                "title": title,
                "price": price,
                "rating": rating,
                "availability": availability
            })

    return pd.DataFrame(all_books)