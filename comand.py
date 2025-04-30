class ComandoEditarTarea:
    def __init__(self, dao, tarea_id, nuevo_titulo, nueva_descripcion):
        self.dao = dao
        self.tarea_id = tarea_id
        self.nuevo_titulo = nuevo_titulo
        self.nueva_descripcion = nueva_descripcion

    def ejecutar(self):
        self.dao.editar(self.tarea_id, self.nuevo_titulo, self.nueva_descripcion)
