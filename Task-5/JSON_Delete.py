import json

with open(r"E:\Darshan_Weneura\Task-5\students_2.json","r") as file:
    students = json.load(file)

students = [
    student for student in students
    if student["id"] != 1
    ]
with open(r"E:\Darshan_Weneura\Task-5\students_2.json","w") as file:
    json.dump(students,file,indent=4)

print("student Deleted!")