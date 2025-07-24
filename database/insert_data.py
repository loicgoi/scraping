import sqlite3
import pandas as pd

# Création de la BDD
def create_db(df_books: pd.DataFrame) -> None:
    """
    Crée une BDD SQLite nommée book_store.db et crée une table book_store avec les données du Dataframe df_books.

    Parameters
    ----------
    df_books : pandas.DataFrame
        Le Dataframe contenant les données du site

    Returns
    -------
    connection : sqlite3.Connection
        La connexion à la BDD book_store
    """
    connection = sqlite3.connect("database/book_store.db")

    # On vérifie que la BDD est créée
    print(connection.total_changes)

    # On crée une table dans la BDD avec le Dataframe
    df_books.to_sql('book_store', connection, if_exists='replace')

    return connection, df_books


# Insérer les données
def insert_data(connection, df_books: pd.DataFrame) -> None:
    """
    Insérer les données dans la base de données book_store

    Parameters
    ----------
    df_books : pandas.DataFrame
        Le dataframe contenant les données du site

    Returns
    -------
    None

    Notes
    -----
    Cette fonction permet d'insérer les données extraites du site dans la base de données.
    Et de compter le nombre de livre dans la base de données.
    """

    # Création d'un curseur pour interagir avec la DB
    cursor = connection.cursor()

    # Exécuter la requête pour compter le nombre de livre dans la DB
    cursor.execute("SELECT COUNT(*) FROM book_store")

    # Affichage du résultat
    print(cursor.fetchone()[0])