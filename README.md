Introduction scraping de données
================================

Ce repo contient les notebooks correspondant au brief [La Plume Libre #3] Extraction de données automatisée pour le site d'une librairie en ligne.


# 📚 Book Scraper

Ce projet est un pipeline de scraping structuré pour extraire, nettoyer et stocker les données des livres du site [books.toscrape.com](http://books.toscrape.com) dans une base de données SQLite.

---

## 🧠 Objectifs du projet

- Scraper les informations des livres (titre, prix, note, disponibilité).
- Nettoyer les données pour un usage ultérieur (analyse, visualisation, etc.).
- Insérer les données dans une base de données locale (`book_store.db`).
- Stocker les données brutes au format CSV (`data/books_infos.csv`).

---

## 📁 Arborescence du projet

=======

```
├── data/
│   ├── data_api.csv                # Données nettoyées au format CSV (API)
│   ├── data_api_raw.csv            # Données brutes au format CSV (API)
│   └── data_scraping.csv           # Données brutes au format CSV (Scraping)
├── database/
│   ├── __init__.py
│   ├── insert_data.py             # Insertion des données dans la base SQLite
│   └── book_store.db              # Base de données SQLite générée
├── get_data/
│   ├── __init__.py
│   ├── get_api_data.py            # Fonction de récupération HTML (API)
│   └── get_scraping_data.py       # Fonction de récupération HTML (Scraping)
├── notebooks/
│   ├── 1_scraping.ipynb           # Notebook pour tests de scraping
│   ├── 2_create_bdd.ipynb         # Notebook pour création de la base
│   └── 3_API_googleBooks.ipynb    # Test d'enrichissement via l'API Google Books
├── pipelines/
│   ├── __init__.py
│   ├── pipeline_api.py            # Pipeline complet d'extraction + insertion (API)
│   └── pipeline_scraping.py       # Pipeline complet d'extraction + insertion (Scraping)
├── process_data/
│   ├── __init__.py
│   ├── process_api_data.py        # Nettoyage et typage des données (API)
│   └── process_scraping_data.py   # Nettoyage et typage des données (Scraping)
├── main.py                        # Script principal à exécuter
├── README.md                      # Documentation du projet
├── requirements.txt

---
```

=======

## ⚙️ Installation

1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/loicgoi/scraping
   
   cd book-scraper

   python -m venv venv

   pip install -r requirements.txt


## ▶️ Lancer le projet

    Dans le fichier main.py, les deux pipelines sont lancés :
        - pipeline Scraping avec un nombre de pages + URL personnalisable ;
        - pipeline API Google Books avec un nombre de résultats = 40.

    from pipelines.pipeline_scraping import run_scraping_pipeline
    from pipelines.pipeline_api import run_api_pipeline

    if __name__ == "__main__":
        # Scraping classique
        run_scraping_pipeline(pages=50)

        # Requête Google Books
        run_api_pipeline(query="data science", max_results=40)
    
    Puis exécuter simplement :

    python main.py

## 💡 Personnalisation
    Pour changer de site, modifiez base_url dans main.py. Assurez-vous que la structure HTML soit compatible avec la fonction parse_books_html().

    Pour scraper plus ou moins de pages, changez la valeur de pages.

## 🧪 Exemple de données extraites
    title	                    price	   rating	availability
    It's Only the Himalayas	    45.17	      2	        True
    Tipping the Velvet	        53.74	      1	        True
    Soumission	                50.10	      1	        True

## 🗃️ Base de données
    Les données nettoyées sont insérées dans une base SQLite locale : db/book_store.db.

    La table principale est nommée book_store.

## 🛠️ Technologies utilisées
    Python 3.10+

    requests, beautifulsoup4, pandas, sqlite3

## 📄 Licence
    Projet à but pédagogique - libre d'utilisation et de modification.

## 🙋‍♀️ Auteurs
    Projet développé par [loicgoi]
    Formation IA - Simplon Montpellier (2025–2026)
