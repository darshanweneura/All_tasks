import json

with open(r"E:\Darshan_Weneura\Task-5\students_2.json","r") as file:
    students = json.load(file)

new = {
    "id": 2,
    "name": "Darshan",
    "course": "Python"
}

students.append(new)

with open(r"E:\Darshan_Weneura\Task-5\students_2.json","w") as file:
    json.dump(students,file,indent=4)

print("student Added")