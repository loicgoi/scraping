import pandas as pd

def parse_books_html(soup) -> pd.DataFrame:

    """
    Extraire les informations des livres d'une page HTML et les stocke dans un DataFrame.

    Args:
        soup (BeautifulSoup): Un objet BeautifulSoup contenant le contenu HTML de la page.

    Returns:
        pd.DataFrame: Un DataFrame contenant les informations extraites des livres.
    """
    # Récupérer les informations des livres
    books = soup.select('article.product_pod')

    # Création des listes pour stocker les données
    titles = []
    prices = []
    ratings = []
    availability = []

    # Parcourir les livres et extraire les données
    for book in books:
        titles.append(book.h3.a['title'])
        prices.append(book.select_one('p.price_color').text.strip())
        ratings.append(book.p['class'][1])  # Exemple: 'Three'
        availability.append(book.select_one('p.instock.availability').text.strip())

    # Création du DataFrame
    df = pd.DataFrame({
        "title": titles,
        "price": prices,
        "rating": ratings,
        "availability": availability,
    })

    return df

def process_scraping_data(df_books: pd.DataFrame) -> pd.DataFrame:
    """
    Convertir les types de colonnes et nettoyer les données extraites du site

    Args:
        df_books (pd.DataFrame): Le DataFrame contenant les données extraites du site

    Returns:
        pd.DataFrame: Le DataFrame nettoyé contenant les données extraites du site.
    """

    # Convertir la colonne title en chaîne
    df_books["title"] = df_books["title"].astype(str)

    # Nettoyer le prix (retirer £ et convertir en float)
    df_books["price"] = df_books["price"].astype(str).str.replace("£", "", regex=False)
    df_books["price"] = df_books["price"].astype(float)

    # Convertir la colonne 'availability' en booléen
    def convert_availability(value):
        """
        Convertir la colonne 'availability en booléen.

        Args:
            value (str): La valeur de la colonne 'availability'.

        Returns:
            bool: True si la valeur est "In stock", False sinon.
        """
        if value == "In stock":
            return True
        return False
    
    df_books["availability"] = df_books["availability"].apply(convert_availability)

    # Nettoyage de 'rating' avant mapping
    df_books["rating"] = df_books["rating"].astype(str).str.strip().str.title()

    # Convertir les notes textuelles en notes numériques
    ratings_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5,
    }
    df_books["rating"] = df_books["rating"].map(ratings_map)

    return df_books