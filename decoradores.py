class TareaDecorator:
    def __init__(self, tarea):
        self.tarea = tarea
        self.icono = '🔔'

    def mostrar(self):
        return self.tarea.mostrar()

    def __getattr__(self, attr):
        return getattr(self.tarea, attr)  # Delegar todo lo no definido al objeto decorado

class TareaIcono(TareaDecorator):
    def __init__(self, tarea):
        super().__init__(tarea)
        self.icono = '☀️'

    def mostrar(self):
        return f"{self.icono} {self.tarea.mostrar()}"
    
    def __getattr__(self, attr):
        return getattr(self.tarea, attr)

