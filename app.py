from flask import Flask, render_template, request, redirect, url_for, g
import sqlite3
import os

# This project uses SQLite for simplicity. Replace with MySQL if needed.
DATABASE = os.path.join(os.path.dirname(__file__), 'data.db')

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def init_db():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS contactos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                correo TEXT NOT NULL,
                celular TEXT,
                horario TEXT
            )
        ''')
        db.commit()

app = Flask(__name__)

@app.before_first_request
def startup():
    init_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/', methods=['GET'])
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    nombre = request.form.get('nombre')
    correo = request.form.get('correo')
    celular = request.form.get('celular')
    horario = request.form.get('horario')
    db = get_db()
    cursor = db.cursor()
    cursor.execute('INSERT INTO contactos (nombre, correo, celular, horario) VALUES (?, ?, ?, ?)',
                   (nombre, correo, celular, horario))
    db.commit()
    return redirect(url_for('gracias'))

@app.route('/gracias')
def gracias():
    return render_template('gracias.html')

@app.route('/dashboard')
def dashboard():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT id, nombre, correo, celular, horario FROM contactos ORDER BY id DESC')
    rows = cursor.fetchall()
    return render_template('dashboard.html', rows=rows)

if __name__ == '__main__':
    # Accessible on local network: host 0.0.0.0, port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
