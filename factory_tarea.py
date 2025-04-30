class TareaBase:
    def __init__(self, id, titulo, descripcion, estado, tipo, fecha_creacion):
        self.id = id
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado
        self.tipo = tipo
        self.fecha_creacion = fecha_creacion

    def mostrar(self):
        return f"{self.titulo} - {self.descripcion} [{self.estado}] ({self.tipo}) [{self.fecha_creacion}]"


class TareaNormal(TareaBase):
    def mostrar(self):
        return f"[Normal] {super().mostrar()}"


class TareaUrgente(TareaBase):
    def mostrar(self):
        return f"[Urgente ⚠️] {super().mostrar()}"


class TareaConFechaLimite(TareaBase):
    def mostrar(self):
        return f"[Con Fecha Límite 🕒] {super().mostrar()}"


class TareaFactory:
    @staticmethod
    def crear_tarea(id, titulo, descripcion, estado, tipo, fecha_creacion):
        tipo = tipo.lower()
        if tipo == "urgente":
            return TareaUrgente(id, titulo, descripcion, estado, tipo,fecha_creacion)
        elif tipo == "fecha_limite":
            return TareaConFechaLimite(id, titulo, descripcion, estado, tipo,fecha_creacion)
        else:
            return TareaNormal(id, titulo, descripcion, estado, tipo,fecha_creacion)
