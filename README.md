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

```
├── data/
│   └── books_infos.csv            # Données brutes au format CSV
├── database/
│   ├── __init__.py
│   ├── insert_data.py             # Insertion des données dans la base SQLite
│   └── book_store.db              # Base de données SQLite générée
├── get_data/
│   ├── __init__.py
│   └── get_scraping_data.py       # Fonction de récupération HTML
├── notebooks/
│   ├── 1_scraping.ipynb           # Notebook pour tests de scraping
│   ├── 2_create_bdd.ipynb         # Notebook pour création de la base
│   └── 3_API_googleBooks.ipynb    # Test d'enrichissement via l'API Google Books
├── pipelines/
│   ├── __init__.py
│   └── pipeline_scraping.py       # Pipeline complet d'extraction + insertion
├── process_data/
│   ├── __init__.py
│   └── process_scraping_data.py   # Nettoyage et typage des données
├── main.py                        # Script principal à exécuter
├── README.md                      # Documentation du projet
├── requirements.txt

---
```

## ⚙️ Installation

1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/loicgoi/scraping
   
   cd book-scraper

   python -m venv venv

   pip install -r requirements.txt


## ▶️ Lancer le projet

    Dans le fichier main.py, le pipeline est lancé avec le nombre de pages à scraper et une URL modifiable :

    from pipelines.pipeline_scraping import run_scraping_pipeline

    if __name__ == "__main__":
        base_url = "http://books.toscrape.com/catalogue/page-{}.html"
        df = run_scraping_pipeline(pages=50, base_url=base_url)
    
    Puis exécuter simplement :

    python main.py

## 💡 Personnalisation
    Pour changer de site, modifiez base_url dans main.py. Assurez-vous que la structure HTML soit compatible avec la fonction parse_books_html().

    Pour scraper plus ou moins de pages, changez la valeur de pages.

## 🧪 Exemple de données extraites
    title	price	rating	availability
    It's Only the Himalayas	45.17	2	True
    Tipping the Velvet	53.74	1	True
    Soumission	50.10	1	True

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