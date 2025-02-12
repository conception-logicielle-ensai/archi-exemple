from typing import Optional
from dao.configuration.database_connector import DatabaseConnector
from business_object.user import User

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
        distinct_roles = list(set(role[0] for role in roles))
        user = User(id=user_dict[0], username=user_dict[1], roles=distinct_roles)
        self.database_connector.close_connection()
        return user

    def save_user(self, name: str,roles:Optional[tuple[str]]) -> int:
        connexion = self.database_connector.get_connection()
        cursor = connexion.cursor()
        cursor.execute("INSERT INTO users (username) VALUES (?)", (name,))
        id = cursor.lastrowid
        if roles is not None:
            for role in roles:
                cursor.execute("INSERT INTO roles_user (user_id,role) VALUES (?,?)", (id,role,))
        connexion.commit()
        return id

    @staticmethod
    def of_context():
        # Parce qu'on a pas vu la configuration
        database_connector = DatabaseConnector("sqlite", "default.db")
        return UserDAO(database_connector=database_connector)

    def get_users(self):
        connexion = self.database_connector.get_connection()
        cursor = connexion.cursor()
        cursor.execute("SELECT u.*, r.role FROM users u JOIN roles_user r on r.user_id = u.id ")
        user_tuple = cursor.fetchall()
        distinct_user_id = list(set(user[0] for user in user_tuple))

        users = []
        for user_id in distinct_user_id:
            def is_tuple_of_user(tuple):
                return str(tuple[0]) == str(user_id)
            get_user_username = lambda tuple_sql: tuple_sql[1]
            get_user_role = lambda tuple_sql: tuple_sql[2]
            users.append(User(id=user_id,username=list(map(get_user_username,filter(is_tuple_of_user,user_tuple)))[0],roles=list(map(get_user_role, filter(is_tuple_of_user,user_tuple)))))
        return users
