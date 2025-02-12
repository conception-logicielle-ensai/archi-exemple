import sqlite3
from typing import Literal, Optional

from utils.singleton import Singleton


class DatabaseConnector(metaclass=Singleton):
    _connection = None

    def __init__(
        self,
        db_type: Literal["sqlite"] = "sqlite",
        db_name: Optional[str] = "default.db",
    ):
        self.db_type = db_type
        self.db_name = db_name
        self.connect()

    def _connect_sqlite(self, db_name):
        try:
            DatabaseConnector._connection = sqlite3.connect(db_name)
        except sqlite3.Error as e:
            print(f"Erreur de connexion SQLite : {e}")

    def connect(self):
        if DatabaseConnector._connection is not None:
            raise RuntimeError("Base de données déjà connectée!")

        if self.db_type == "sqlite":
            self._connect_sqlite(self.db_name)
        else:
            raise ValueError(
                "Type de base de données inconnu. Choisissez 'sqlite' ou '?'."
            )

    def init_db(self):
        if self.db_type == "sqlite":
            connexion = self.get_connection()
            cursor = connexion.cursor()
            # creation table users
            cursor.execute("""DROP TABLE IF EXISTS users;""")
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL UNIQUE
                    );"""
            )
            cursor.execute("""DROP TABLE IF EXISTS roles_user;""")
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS roles_user (
                        user_id INTEGER NOT NULL,
                        role TEXT NOT NULL,
                        FOREIGN KEY (user_id) REFERENCES users (id)
                    );"""
            )
            connexion.commit()
            # Insertion d'un utilisateur 'admin'
            cursor.execute("INSERT INTO users (username) VALUES (?)", ("adm",))
            user_id = cursor.lastrowid  # Récupère l'id du nouvel utilisateur
            # Insertion du rôle 'admin' pour cet utilisateur
            cursor.execute(
                "INSERT INTO roles_user (user_id, role) VALUES (?, ?)",
                (user_id, "admin"),
            )
            cursor.execute(
                "INSERT INTO roles_user (user_id, role) VALUES (?, ?)", (user_id, "dev")
            )
            connexion.commit()
            user_id = cursor.lastrowid
            cursor.execute("INSERT INTO users (username) VALUES (?)", ("pasadm",))
            cursor.execute(
                "INSERT INTO roles_user (user_id, role) VALUES (?, ?)", (user_id, "dev")
            )
            # Commit des changements
            connexion.commit()
            self.close_connection()

    def get_connection(self):
        if DatabaseConnector._connection is None:
            self.connect()
        return DatabaseConnector._connection

    def close_connection(self):
        """Ferme la connexion à la base de données si elle est ouverte."""
        if DatabaseConnector._connection is not None:
            DatabaseConnector._connection.close()
            DatabaseConnector._connection = None
