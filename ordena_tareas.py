from abc import ABC, abstractmethod
from datetime import datetime

class ordena_tareas(ABC):
    @abstractmethod
    def ordenar(self, tareas):
        pass

class OrdenarFechaASC(ordena_tareas):
    def ordenar(self, tareas):
        return sorted(tareas, key=lambda t: t.fecha_creacion or datetime.max)

class OrdenarFechaDES(ordena_tareas):
    def ordenar(self, tareas):
        return sorted(tareas, key=lambda t: t.fecha_creacion or datetime.min, reverse=True)