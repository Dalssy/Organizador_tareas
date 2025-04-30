from flask import Blueprint, render_template, request, redirect, url_for, session
from dao_tareas import TareaDAO
from factory_tarea import TareaFactory
from ordena_tareas import OrdenarFechaASC
from decoradores import TareaIcono
from comand import ComandoEditarTarea
ordenador = OrdenarFechaASC()

dashboard_bp = Blueprint('dashboard', __name__)
tarea_dao = TareaDAO('tareas.db')  # Singleton se aplica internamente

#tareas_ordenadas = ''
@dashboard_bp.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'id' not in session:
        return redirect(url_for('login'))

    usuario_id = session['id']  
    if request.method == 'POST':
        titulo = request.form['titulo']
        descripcion = request.form['descripcion']
        tarea_dao.agregar(titulo, descripcion, usuario_id)
        return redirect(url_for('dashboard.dashboard'))
    
    # Obtener tareas y ordenarlas
    tareas = tarea_dao.obtener_tareas_por_usuario(usuario_id)
    tareas_ordenadas = ordenador.ordenar(tareas)

    tareas_decoradas = []
    for tarea in tareas_ordenadas:
        if tarea.tipo.lower() == "urgente":
            tarea = TareaIcono(tarea)
        tareas_decoradas.append(tarea)

    return render_template('dashboard.html', tareas=tareas_decoradas)


@dashboard_bp.route('/completar/<int:tarea_id>')
def completar_tarea(tarea_id):
    tarea_dao.completar(tarea_id)
    return redirect(url_for('dashboard.dashboard'))

@dashboard_bp.route('/eliminar/<int:tarea_id>')
def eliminar_tarea(tarea_id):
    tarea_dao.eliminar(tarea_id)
    return redirect(url_for('dashboard.dashboard'))

@dashboard_bp.route('/actualizar_tipo', methods=['POST'])
def actualizar_tipo():
    #conn = DatabaseConnection.get_instance(self.db_name)
    #cursor =conn.cursor()
    #cursor.execute ("UPDATE tareas SET tipo = ? WHERE id = ?", (nuevo_tipo, id_tarea))
    #conn.commit()

    id_tarea = int(request.form['id'])
    nuevo_tipo = request.form['tipo']
         
    tarea_dao.actualizar_tipo(id_tarea, nuevo_tipo)

    return redirect(url_for('dashboard.dashboard'))

@dashboard_bp.route('/editar_tarea', methods=['POST'])
def editar_tarea():
    id_tarea = int(request.form['id'])
    nuevo_titulo = request.form['titulo']
    nueva_descripcion = request.form['descripcion']

    comando = ComandoEditarTarea(tarea_dao, id_tarea, nuevo_titulo, nueva_descripcion)
    comando.ejecutar()

    return redirect(url_for('dashboard.dashboard'))




