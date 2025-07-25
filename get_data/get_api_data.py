import requests

def search_books(params: dict = None, min_rating: int = 1, desired_results: int = 40, query: str = "") -> list:
    """
    Interroge l’API Google Books et retourne une liste filtrée de livres.

    Parameters
    ----------
    params : dict, optional
        Paramètres de la requête.
    min_rating : float, optional
        Note minimale souhaitée.
    desired_results : int, optional
        Nombre de résultats filtrés désirés.
    query : str, optional
        Mot-clé pour filtrer manuellement titre et catégories.

    Returns
    -------
    list
        Liste de livres filtrés.
    """

    if params is None:
        params = {
            "q": query or "food",
            "filter": "paid-ebooks",
            "maxResults": 40,
            "orderBy": "relevance"
        }

    url = "https://www.googleapis.com/books/v1/volumes"
    collected_books = []
    start_index = 0
    query_lower = query.lower()

    while len(collected_books) < desired_results:
        params["startIndex"] = start_index
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        items = data.get("items", [])
        if not items:
            break

        for book in items:
            volume_info = book.get("volumeInfo", {})
            rating = volume_info.get("averageRating")

            # Filtrer sur le rating minimal
            if rating is None or rating < min_rating:
                continue

            title = volume_info.get("title", "").lower()
            categories = " ".join(volume_info.get("categories", [])).lower()

            # Filtrage manuel sur le query dans titre ou catégories
            if query_lower not in title and query_lower not in categories:
                continue

            collected_books.append(book)
            if len(collected_books) >= desired_results:
                break

        start_index += params.get("maxResults", 40)

    return collected_books
