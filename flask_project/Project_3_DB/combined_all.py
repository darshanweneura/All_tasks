import sqlite3

DB_NAME = r"C:\Users\Deval\OneDrive\Documents\GitHub\Python-Tasks\flask_project\Project_3_DB\students_2.db"

def connect_db():
    return sqlite3.connect(DB_NAME)

def create_table():
    connection = connect_db()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                course TEXT
            )
            """)
        connection.commit()

        print("Table is created")

    except sqlite3.Error as e:
        connection.rollback()
        print("Error : ", e)

    finally:
        connection.close()

def add_student(name,age,course):
    connection = connect_db()

    try:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO students (name, age, course)
            VALUES (?, ?, ?)
            """, (name, age, course))

        connection.commit()

        print("Student added")

    except sqlite3.Error as e:
        connection.rollback()
        print("error: ", e)
    finally:
        connection.close()

def get_student():
    connection = connect_db()

    try:
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM students")

        students = cursor.fetchall()

        for i in students:
            print(i)

    except sqlite3.Error as e:
        print("Error: ",e)

    finally:
        connection.close()

def get_student_by_id(student_id):
    connection = connect_db()

    try:
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM students WHERE id = ?",
            (student_id,)
        )

        student = cursor.fetchone()

        print(student)

    except sqlite3.Error as e:
        print("Error: ",e)

    finally:
        connection.close()

def update_student_age(student_id,age):
    connection = connect_db()

    try:
        cursor = connection.cursor()

        cursor.execute("UPDATE students SET age = ? WHERE id = ?",
            (age,student_id)
        )

        connection.commit()

        print("Student Updated")

    except sqlite3.Error as e:
        connection.rollback()
        print("Error: ",e)

    finally:
        connection.close()

def delete_student(student_id):
    connection = connect_db()

    try:
        cursor = connection.cursor()

        cursor.execute("DELETE FROM students WHERE id = ?",
            (student_id,)
        )

        connection.commit()
        print("Student Deleted")

    except sqlite3.Error as e:
        connection.rollback()
        print("Error: ",e)

    finally:
        connection.close()

create_table()
add_student('darshan',20,'Python')
add_student('Krishna',21,'Data_Analyst')
add_student('nandani',21,'Full Stack')

print("\n All students:")
get_student()

print("\n Search student:")
get_student_by_id(1)

print("\n update student:")
update_student_age(1,21)

print("\nDelete Student:")
delete_student(2)

print("\nFinal Student List:")
get_student()