import pandas as pd

def process_api_data(raw_json: dict) -> pd.DataFrame:
    """
    Nettoie la réponse Google Books et retourne un DataFrame avec
    les colonnes : index, title, price, rating, availability
    - Les lignes contenant des NULL sont supprimées
    - L'index commence après la dernière ligne du scraping

    Args:
        raw_json (dict): Dictionnaire contenant les données brutes de Google Books

    Returns:
        pd.DataFrame: DataFrame nettoyé contenant les colonnes :
            index, title, price, rating, availability
    """

    # Extraire les données
    items = raw_json.get("items", [])
    books = []

    # Nettoyer les données
    for item in items:
        volume_info = item.get("volumeInfo", {})
        sale_info = item.get("saleInfo", {})

        title = volume_info.get("title")
        price = sale_info.get("listPrice", {}).get("amount")
        rating = volume_info.get("averageRating")
        availability = sale_info.get("saleability") == "FOR_SALE"

        if title is None:
            continue # Passer au livre suivant si le titre est manquant

        books.append({
            "title": title,
            "price": price,
            "rating": rating,
            "availability": availability
        })

    # Créer le DataFrame
    df = pd.DataFrame(books)

    # Supprimer les lignes sans prix ou rating
    df = df.dropna(subset=["price", "rating"])

    # Convertir rating en int (en arrondissant ou tronquant)
    df["rating"] = df["rating"].astype(int)

    return df