from db_singleton import DatabaseConnection
from factory_tarea import TareaFactory


class TareaDAO:
    def __init__(self, db_name='tareas.db'):
        self.db_name = db_name
        self.crear_tabla()

    def crear_tabla(self):
        conn = DatabaseConnection.get_instance(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS tareas (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            titulo TEXT NOT NULL,
                            descripcion TEXT NOT NULL,
                            estado TEXT DEFAULT 'pendiente',
                            tipo TEXT DEFAULT 'normal',
                            usuario_id INTEGER,
                            fecha_creacion	TEXT DEFAULT CURRENT_TIMESTAMP)''')
        conn.commit()


    def obtener_tareas_por_usuario(self, usuario_id):
        conn = DatabaseConnection.get_instance(self.db_name) #NO CAMBIAR
        cursor = conn.cursor()
        cursor.execute("SELECT id, titulo, descripcion, estado, tipo,fecha_creacion FROM tareas WHERE usuario_id = ?", (usuario_id,))
        tareas_crudas = cursor.fetchall()


        tareas = [TareaFactory.crear_tarea(*fila) for fila in tareas_crudas]
        return tareas

    def agregar(self, titulo, descripcion, usuario_id):
        conn = DatabaseConnection.get_instance(self.db_name)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tareas (titulo, descripcion, estado, usuario_id, fecha_creacion) VALUES (?, ?, ?, ?, datetime ('now'))",
                       (titulo, descripcion, "pendiente", usuario_id))
        conn.commit()


    def completar(self, tarea_id):
        conn = DatabaseConnection.get_instance(self.db_name)
        cursor = conn.cursor()
        cursor.execute("UPDATE tareas SET estado = 'completada' WHERE id = ?", (tarea_id,))
        conn.commit()

    def eliminar(self, tarea_id):
        conn = DatabaseConnection.get_instance(self.db_name)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tareas WHERE id = ?", (tarea_id,))
        conn.commit()

    def editar(self, id_tarea, nuevo_titulo, nueva_descripcion):
        conn = DatabaseConnection.get_instance(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE tareas
            SET titulo = ?, descripcion = ?
            WHERE id = ?
        """, (nuevo_titulo, nueva_descripcion, id_tarea))
        conn.commit()

    def actualizar_tipo(self, id_tarea, nuevo_tipo):
        conn = DatabaseConnection.get_instance(self.db_name)
        cursor = conn.cursor()
        cursor.execute("UPDATE tareas SET tipo = ? WHERE id = ?", (nuevo_tipo, id_tarea))
        conn.commit()
