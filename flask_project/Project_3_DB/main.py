import sqlite3

connection = sqlite3.connect(r"C:\Users\Deval\OneDrive\Documents\GitHub\Python-Tasks\flask_project\Project_3\students.db")

print("Database connected successfully!")

connection.close()