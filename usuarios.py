import hashlib
from db_singleton import DatabaseConnection

class UsuarioDAO:
    def __init__(self, db_path='tareas.db'):
        self.db_path = db_path
        self.crear_tabla()

    def crear_tabla(self):
        conn = DatabaseConnection.get_instance(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT UNIQUE NOT NULL,
                            password_hash TEXT NOT NULL)''')
        conn.commit()

    def agregar_usuario(self, username, password):
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        try:
            conn = DatabaseConnection.get_instance(self.db_path)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO usuarios (username, password_hash) VALUES (?, ?)", 
                           (username, password_hash))
            conn.commit()
            print(f"[✔] Usuario '{username}' creado exitosamente.")
        except Exception as e:
            print(f"[✘] Error: {e}")

    def verificar_usuario(self, username, password):
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        conn = DatabaseConnection.get_instance(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE username = ? AND password_hash = ?", 
                       (username, password_hash))
        user = cursor.fetchone()
        return user is not None
