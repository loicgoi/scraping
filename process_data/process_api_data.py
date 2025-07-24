import pandas as pd

def process_api_data(raw_json: dict) -> pd.DataFrame:
    """
    Nettoie la réponse Google Books et retourne un DataFrame avec
    les colonnes : index, title, price, rating, availability
    - Les lignes contenant des NULL sont supprimées
    - L'index commence après la dernière ligne du scraping
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
        rating = volume_info.get("averageRating", 0)
        availability = sale_info.get("saleability") == "FOR_SALE"

        books.append({
            "title": title,
            "price": price,
            "rating": rating,
            "availability": availability
        })

    # Créer le DataFrame
    df = pd.DataFrame(books)

    # Supprimer les NULL
    df = df.dropna(subset=["price", "rating"])

    # Convertir les types
    df["rating"] = df["rating"].astype(float)

    # Continuer l’index après le scraping
    last_scraping_idx = 999  # on sait que le scraping s’arrête à 999
    df.index = range(last_scraping_idx + 1, last_scraping_idx + 1 + len(df))

    return df