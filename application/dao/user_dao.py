from application.dao.configuration.database_connector import DatabaseConnector


class UserDAO:
    def __init__(self, database_connector:DatabaseConnector):
        self.database_connector = database_connector
    def get_user_by_username(self, username:str ) :
        connexion = self.database_connector.get_connection()
        cursor = connexion.cursor() 
        cursor.execute("SELECT * FROM users a WHERE username = ?", (username,))
        user_dict = cursor.fetchone()
        if user_dict is None:
            raise ValueError(f"Pas d'utilisateur avec username {username}")
        cursor.execute("SELECT role from roles_user where user_id = ?",(str(user_dict[0])))
        roles = cursor.fetchall()
        distinct_roles = list(set(role[0] for role in roles))
        user = User(id=user_dict[0], username=user_dict[1],roles=distinct_roles)
        self.database_connector.close_connection()
        return user
    def save_user(self, name: str, email: str) -> int:
        cursor = self._conn.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        self._conn.commit()
        return cursor.lastrowid
    @staticmethod
    def of_context():
        # Parce qu'on a pas vu la configuration
        database_connector = DatabaseConnector("sqlite","default.db")
        return UserDAO(database_connector=database_connector)