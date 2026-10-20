# ==============================
# app.py
# Hospital Management System
# ==============================

from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(_name_)

# ---------------- DATABASE ----------------

def init_db():
    conn = sqlite3.connect('hospital.db')
    cur = conn.cursor()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        disease TEXT,
        address TEXT,
        room TEXT
    )
    ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS doctors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        specialization TEXT
    )
    ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS staff (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        position TEXT
    )
    ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS rooms (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        room_no TEXT,
        room_type TEXT,
        price INTEGER
    )
    ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS bills (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_name TEXT,
        medicine_cost INTEGER,
        operation_cost INTEGER,
        total INTEGER
    )
    ''')

    conn.commit()
    conn.close()

init_db()

# ---------------- HOME ----------------

@app.route('/')
def home():
    return render_template('index.html')

# ---------------- PATIENTS ----------------

@app.route('/patients', methods=['GET', 'POST'])
def patients():

    conn = sqlite3.connect('hospital.db')
    cur = conn.cursor()

    if request.method == 'POST':

        name = request.form['name']
        age = request.form['age']
        disease = request.form['disease']
        address = request.form['address']
        room = request.form['room']

        cur.execute('''
        INSERT INTO patients(name, age, disease, address, room)
        VALUES (?, ?, ?, ?, ?)
        ''', (name, age, disease, address, room))

        conn.commit()

    cur.execute('SELECT * FROM patients')
    data = cur.fetchall()

    conn.close()

    return render_template('patients.html', patients=data)

# ---------------- DELETE PATIENT ----------------

@app.route('/delete_patient/<int:id>')
def delete_patient(id):

    conn = sqlite3.connect('hospital.db')
    cur = conn.cursor()

    cur.execute('DELETE FROM patients WHERE id=?', (id,))
    conn.commit()

    conn.close()

    return redirect('/patients')

# ---------------- DOCTORS ----------------

@app.route('/doctors', methods=['GET', 'POST'])
def doctors():

    conn = sqlite3.connect('hospital.db')
    cur = conn.cursor()

    if request.method == 'POST':

        name = request.form['name']
        specialization = request.form['specialization']

        cur.execute('''
        INSERT INTO doctors(name, specialization)
        VALUES (?, ?)
        ''', (name, specialization))

        conn.commit()

    cur.execute('SELECT * FROM doctors')
    data = cur.fetchall()

    conn.close()

    return render_template('doctors.html', doctors=data)

# ---------------- STAFF ----------------

@app.route('/staff', methods=['GET', 'POST'])
def staff():

    conn = sqlite3.connect('hospital.db')
    cur = conn.cursor()

    if request.method == 'POST':

        name = request.form['name']
        position = request.form['position']

        cur.execute('''
        INSERT INTO staff(name, position)
        VALUES (?, ?)
        ''', (name, position))

        conn.commit()

    cur.execute('SELECT * FROM staff')
    data = cur.fetchall()

    conn.close()

    return render_template('staff.html', staff=data)

# ---------------- ROOMS ----------------

@app.route('/rooms', methods=['GET', 'POST'])
def rooms():

    conn = sqlite3.connect('hospital.db')
    cur = conn.cursor()

    if request.method == 'POST':

        room_no = request.form['room_no']
        room_type = request.form['room_type']
        price = request.form['price']

        cur.execute 
