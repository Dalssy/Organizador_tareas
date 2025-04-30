import sqlite3

class DatabaseConnection:
    _instance = None

    def __init__(self, db_name='tareas.db'):
        if not hasattr(self, 'conn'):
            self.conn = sqlite3.connect(db_name, check_same_thread=False)  
            self.conn.row_factory = sqlite3.Row  
             
    @classmethod
    def get_instance(cls, db_name='tareas.db'):
        if cls._instance is None:
            cls._instance = cls(db_name)
        return cls._instance.conn
