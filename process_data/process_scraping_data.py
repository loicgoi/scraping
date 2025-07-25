import pandas as pd

def process_scraping_data(df_books: pd.DataFrame) -> pd.DataFrame:
    """
    Nettoie et convertit les colonnes d'un DataFrame brut de livres en types appropriés.

    Étapes effectuées :
    - Conversion de la colonne `title` en chaîne de caractères
    - Nettoyage et conversion de la colonne `price` en float
    - Conversion de la colonne `availability` en booléen
    - Mapping de la colonne `rating` (texte → entier de 1 à 5)

    Args:
        df_books (pd.DataFrame): DataFrame brut contenant les colonnes :
            title, price, rating, availability

    Returns:
        pd.DataFrame: DataFrame nettoyé avec les types convertis :
            - title (str)
            - price (float)
            - rating (int)
            - availability (bool)

    Exemple:
        >>> df = pd.DataFrame([{"title": "A Book", "price": "£10.99", "rating": "Three", "availability": "In stock"}])
        >>> process_scraping_data(df)
           title  price  rating  availability
        0 A Book  10.99       3          True
    """

    # Conversion de title en chaîne de caractères
    df_books["title"] = df_books["title"].astype(str)
    df_books["price"] = df_books["price"].str.replace("£", "", regex=False).astype(float)

    def convert_availability(value):
        """
        Convertir la colonne availability en booléen

        Args:
            value (str): Statut du livre si disponible ou non

        Returns:
            bool: True si disponible, False sinon.
        """
        return value == "In stock"

    # Conversion de availability en booléen
    df_books["availability"] = df_books["availability"].apply(convert_availability)

    # Mapping de la colonne rating
    ratings_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5,
    }
    df_books["rating"] = df_books["rating"].map(ratings_map).astype(int)  # Application du mapping de la colonne rating

    return df_books