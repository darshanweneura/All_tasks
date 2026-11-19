import sqlite3

connection = None

try:
    connection = sqlite3.connect(r"C:\Users\Deval\OneDrive\Documents\GitHub\Python-Tasks\flask_project\Project_3\students_3.db")
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO students (name,age,course)
        VALUES(?,?,?)""", ('darshan',20,'Java'))

    connection.commit()

    print("student inserted")

except sqlite3.Error as e:
    if connection:
        connection.rollback()
    print("Database error:", e)

finally:
    if connection:
        connection.close()