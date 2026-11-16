import json

student = {
    "name": "Krishna",
    "age": 20,
    "course": "Python",
    "city": "Rajkot"
}

with open(r"E:\Darshan_Weneura\Task-5\students.json", "a") as file:

    json.dump(student, file, indent=4)

print("Data saved successfully!")

with open(r"E:\Darshan_Weneura\Task-5\students.json" ,"r" ) as file:
        print(file.read())