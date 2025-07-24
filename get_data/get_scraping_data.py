import requests
from bs4 import BeautifulSoup

def scrape_books(pages: int, base_url: str) -> list[dict]:
    """
    Scrape les informations des livres sur plusieurs pages.

    Args:
        pages (int): Nombre de pages à scraper.
        base_url (str): URL de base avec `{}` pour insérer le numéro de page, exemple:
                        "http://books.toscrape.com/catalogue/page-{}.html"

    Returns:
        list[dict]: Liste des dictionnaires contenant les informations des livres.
    """
    all_books = []

    for page_num in range(1, pages + 1):
        url = base_url.format(page_num)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        book_elements = soup.select("article.product_pod")  # À adapter selon le site
        data_books = [extract_book_info(book) for book in book_elements]
        all_books.extend(data_books)

    return all_books


