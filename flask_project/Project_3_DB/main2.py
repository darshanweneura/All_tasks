import sqlite3

connection = sqlite3.connect(r"C:\Users\Deval\OneDrive\Documents\GitHub\Python-Tasks\flask_project\Project_3\students_2.db")

cursor = connection.cursor()

cursor.execute("SELECT sqlite_version()")

result = cursor.fetchone()

print(result)

connection.close()