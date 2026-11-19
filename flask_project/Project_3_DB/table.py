import sqlite3

connection = sqlite3.connect(r"C:\Users\Deval\OneDrive\Documents\GitHub\Python-Tasks\flask_project\Project_3\students_3.db")
cursor = connection.cursor()

cursor.execute("""
    INSERT INTO students (name, age, course)
    VALUES ('Darshan', 21, 'Python')
    """
)
connection.commit()
cursor.execute("SELECT * FROM students")

student = cursor.fetchall()

print(student)

connection.close()