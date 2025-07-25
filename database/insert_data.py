import sqlite3
import pandas as pd
import os

def create_db(df_books: pd.DataFrame) -> sqlite3.Connection:
    """
    Crée une base de données SQLite dans le dossier `database/` et insère les données
    du DataFrame dans une table nommée `book_store`.

    Si le dossier `database/` n'existe pas, il est créé automatiquement.

    Args:
        df_books (pd.DataFrame): DataFrame nettoyé des livres à insérer.

    Returns:
        sqlite3.Connection: Connexion ouverte à la base de données `book_store.db`.

    Exemple:
        >>> conn = create_db(df)
        >>> conn.execute("SELECT COUNT(*) FROM book_store").fetchone()
        (50,)
    """

    # Connexion à la BDD
    conn = sqlite3.connect("database/book_store.db")
    cursor = conn.cursor()

    # Création manuelle de la table si elle n'existe pas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS book_store (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            price REAL,
            availability TEXT,
            rating TEXT
        )
    """)
    conn.commit()

    # Insertion des données dans la table `book_store`
    df_books.to_sql("book_store", conn, if_exists="append", index=False)
    
    return conn

def insert_data(conn: sqlite3.Connection) -> None:
    """
    Affiche le nombre de livres présents dans la table `book_store` de la base SQLite.

    Cette fonction permet de vérifier que l'insertion des données s'est bien déroulée.

    Args:
        conn (sqlite3.Connection): Connexion ouverte à la base de données.

    Returns:
        None
    """

    # Exécuter la requête pour compter le nombre de livre dans la DB
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM book_store")
    count = cursor.fetchone()[0]
    print(f"Nombre de livres insérés en base : {count}")