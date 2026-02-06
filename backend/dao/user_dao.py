import sqlite3
from typing import Optional

from business_object.user import User
from dao.configuration.database_connector import DatabaseConnector
from dao.exceptions import DuplicateEntityError


class UserDAO:
    def __init__(self, database_connector: DatabaseConnector):
        self.database_connector = database_connector

    def get_user_by_username(self, username: str):
        connexion = self.database_connector.get_connection()
        cursor = connexion.cursor()
        cursor.execute("SELECT * FROM users a WHERE username = ?", (username,))
        user_dict = cursor.fetchone()
        if user_dict is None:
            raise ValueError(f"Pas d'utilisateur avec username {username}")
        cursor.execute(
            "SELECT role from roles_user where user_id = ?", (str(user_dict[0]))
        )
        roles = cursor.fetchall()
        distinct_roles = list({role[0] for role in roles})
        user = User(id=user_dict[0], username=user_dict[1], roles=distinct_roles)
        return user

    def save_user(self, name: str, roles: Optional[tuple[str]]) -> int:
        connexion = self.database_connector.get_connection()
        cursor = connexion.cursor()
        try:
            cursor.execute("INSERT INTO users (username) VALUES (?)", (name,))
            id = cursor.lastrowid
            if roles is not None:
                for role in roles:
                    cursor.execute(
                        "INSERT INTO roles_user (user_id,role) VALUES (?,?)",
                        (
                            id,
                            role,
                        ),
                    )
            connexion.commit()
            return id
        except sqlite3.IntegrityError as e:
            if "UNIQUE constraint failed" in str(e):
                raise DuplicateEntityError("username already exists") from e
            raise

    @staticmethod
    def of_context():
        # Parce qu'on a pas vu la configuration
        database_connector = DatabaseConnector("sqlite", "default.db")
        return UserDAO(database_connector=database_connector)

    def get_users(self):
        connexion = self.database_connector.get_connection()
        cursor = connexion.cursor()
        cursor.execute(
            """
            SELECT u.id, u.username, r.role
            FROM users u
            LEFT JOIN roles_user r ON r.user_id = u.id
            """
        )
        rows = cursor.fetchall()
        users_by_id: dict[str, dict[str, set[str]]] = {}
        for row in rows:
            user_id = row[0]
            username = row[1]
            role = row[-1]

            entry = users_by_id.setdefault(
                user_id,
                {"username": username, "roles": set()},
            )
            entry["roles"].add(role)
        users = [
            User(
                id=user_id,
                username=data["username"],
                roles=list(data["roles"]),
            )
            for user_id, data in users_by_id.items()
        ]
        return users
