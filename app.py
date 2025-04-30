from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
from dao_tareas import TareaDAO
from dashboard import dashboard_bp  # Aquí está la lógica del dashboard

tarea_dao = TareaDAO('tareas.db')  # Ya lo usas dentro del blueprint también
app = Flask(__name__)
app.secret_key = 'secreto-supersecreto'

# Registrar blueprint
app.register_blueprint(dashboard_bp)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('tareas.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            session['id'] = user[0]
            return redirect(url_for('dashboard.dashboard'))  # nombre del blueprint + función
        else:
            return render_template('login.html')

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password_confirm = request.form['password_confirm']

        if password != password_confirm:
            return "Las contraseñas no coinciden", 400

        conn = sqlite3.connect('tareas.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM usuarios WHERE username = ?", (username,))
        if cursor.fetchone():
            return "El nombre de usuario ya existe", 400

        cursor.execute("INSERT INTO usuarios (username, password, rol) VALUES (?, ?, ?)", (username, password, 'user'))
        conn.commit()
        conn.close()

        return redirect(url_for('login'))

    return render_template('registro.html')


if __name__ == '__main__':
    app.run(debug=True)
