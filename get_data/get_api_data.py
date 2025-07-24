import requests

def search_books(params: dict = None) -> dict:
    """
    Interroge l’API Google Books.

    Parameters
    ----------
    params : dict, optional
        Paramètres de la requête.

    Returns
    -------
    dict
        Réponse JSON brute de l’API.
    """

    # Paramètres par défaut
    if params is None:
        params = {
            "q": "food",
            "filter": "paid-ebooks",
            "maxResults": 40,
            "orderBy": "relevance"
        }
    
    # URL de l'API
    url = "https://www.googleapis.com/books/v1/volumes"
    
    # Requête vers l'API
    response = requests.get(url, params=params)
    
    # Vérification du code de statut
    response.raise_for_status()
    
    return response.json()