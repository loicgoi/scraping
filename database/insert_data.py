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

    os.makedirs("database", exist_ok=True)
    conn = sqlite3.connect("database/book_store.db")
    df_books.to_sql("book_store", conn, if_exists="replace", index=False)
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

    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM book_store")
    count = cursor.fetchone()[0]
    print(f"Nombre de livres insérés en base : {count}")