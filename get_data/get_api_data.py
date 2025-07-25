import requests
import time

def search_books(params: dict = None, min_rating: int = 1, desired_results: int = 40, query: str = "") -> list:
    """
    Récupère une liste de livres correspondant à une requête via l'API Google Books,
    en filtrant par note minimale et en limitant le nombre total de résultats et de pages consultées.

    Paramètres :
    ----------
    query : str
        Terme de recherche pour les livres.
    min_rating : float, optionnel (par défaut = 3)
        Note minimale (averageRating) requise pour inclure un livre.
    max_results : int, optionnel (par défaut = 100)
        Nombre maximum de livres à collecter au total.
    max_pages : int, optionnel (par défaut = 20)
        Nombre maximum de pages (requêtes API) à interroger pour éviter une surcharge ou un blocage.

    Retourne :
    ---------
    list
        Liste de livres (dictionnaires JSON) répondant aux critères.

    Notes :
    ------
    - Une pause de 1 seconde est insérée entre chaque requête pour éviter une surcharge de l'API.
    - La boucle s'arrête dès que le nombre souhaité de livres est atteint ou qu'il n'y a plus de résultats.
    - Si trop peu de livres correspondent aux critères, le résultat peut être incomplet.
    """

    if params is None:
        params = {
            "q": query or "food",
            "filter": "paid-ebooks",
            "maxResults": 40,
            "orderBy": "relevance"
        }

    # URL de l'API
    url = "https://www.googleapis.com/books/v1/volumes"

    # Collecte des livres
    collected_books = []
    start_index = 0
    query_lower = query.lower()

    # Limitation de pages
    max_pages = 20
    pages_loaded = 0

    # Pagination et filtrage des livres par rating et query
    while len(collected_books) < desired_results and pages_loaded < max_pages:
        params["startIndex"] = start_index
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        items = data.get("items", [])
        if not items:
            break

        # Limitation de pages par rapport au nombre de livres trouvés
        pages_loaded += 1
        time.sleep(1)

        # Filtrage des livres par rating
        for book in items:
            volume_info = book.get("volumeInfo", {})
            rating = volume_info.get("averageRating")

            # Filtrer sur le rating minimal
            if rating is None or rating < min_rating:
                continue

            # Filtrage manuel sur le query dans titre ou catégories
            title = volume_info.get("title", "").lower()
            categories = " ".join(volume_info.get("categories", [])).lower()

            if query_lower not in title and query_lower not in categories:
                continue

            # Ajout du livre aux livres collectés
            collected_books.append(book)
            if len(collected_books) >= desired_results:
                break
        
        # Passage au livre suivant
        start_index += params.get("maxResults", 40)

    return collected_books
