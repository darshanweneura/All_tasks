import sqlite3
from pathlib import Path
from flask import Flask, g, redirect, url_for, render_template, request

app = Flask(__name__)

DB_NAME = Path(__file__).parent / "students.db"

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DB_NAME)
        g.db.row_factory = sqlite3.Row

    return g.db

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Create_DB')
def init_db():
    db = sqlite3.connect(DB_NAME)

    db.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            course TEXT
        )
    """)

    db.commit()
    db.close()
    return "Database and table created successfully!"

@app.route('/add', methods = ["GET","POST"])
def add_student():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        course = request.form["course"]

        db = get_db()
        db.execute(
            """
            INSERT INTO students (name,age,course)
            VALUES (?, ?, ?)
            """,
            (name,age,course)
        )
        db.commit()
        return redirect(url_for("students"))
    return render_template('add_student.html')


@app.route("/students")
def students():
    db = get_db()

    students = db.execute(
        "SELECT * FROM students"
    ).fetchall()

    return str([dict(student) for student in students])

@app.teardown_appcontext
def close_db(error=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run(debug=True)