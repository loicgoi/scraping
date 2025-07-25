import requests

def search_books(params: dict = None, min_rating: int = 0, desired_results: int = 40) -> list:
    """
    Interroge l’API Google Books et retourne une liste de livres avec un rating minimal.

    Parameters
    ----------
    params : dict, optional
        Paramètres de la requête.
    min_rating : float, optional
        Note minimale souhaitée (default: 0 = tous les livres).
    desired_results : int, optional
        Nombre de résultats filtrés désirés (par défaut 40).

    Returns
    -------
    list
        Liste de livres (dictionnaires) avec un rating >= min_rating.
    """

    # Paramètres par défaut
    if params is None:
        params = {
            "q": "food",
            "filter": "paid-ebooks",
            "maxResults": 40,
            "orderBy": "relevance"
        }

    url = "https://www.googleapis.com/books/v1/volumes"
    collected_books = []
    start_index = 0

    while len(collected_books) < desired_results:
        # Mise à jour du startIndex pour paginer
        params["startIndex"] = start_index
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        items = data.get("items", [])
        if not items:
            break  # plus de livres disponibles

        # Filtrage sur le rating
        for book in items:
            rating = book.get("volumeInfo", {}).get("averageRating")
            if rating is not None and rating >= min_rating:
                collected_books.append(book)
                if len(collected_books) >= desired_results:
                    break

        start_index += params.get("maxResults", 40)  # passer à la page suivante

    return collected_books
