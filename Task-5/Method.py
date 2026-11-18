import json
import API_calling as AC
class Employee:

    def __init__(self, name, emp_id, salary, department): 
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
        self.department = department

        self.save_to_file()


    def save_to_file(self): #save to database file
        with open(r"E:\Darshan_Weneura\Task-5\DATA.json","r") as file:
            emp = json.load(file)
            new = {
            "Name": self.name,
            "Employee id": self.emp_id,
            "Salary": self.salary,
            "Department": self.department,
            
            }
            emp.append(new)
        with open(r"E:\Darshan_Weneura\Task-5\DATA.json","w") as file:
            json.dump(emp,file,indent=4)

    def display(self): # display for confirming
        print("\n--- Employee Details ---")
        print("Name:", self.name)
        print("ID:", self.emp_id)
        print("Salary:", self.salary)
        print("Department:", self.department)

    @staticmethod
    def get_last_employee_id():
       
        try:
            with open(r"E:\Darshan_Weneura\Task-5\DATA.json", "r") as file:
                emp = json.load(file)

                if emp:
                    return emp[-1]["Employee id"]

        except (FileNotFoundError, json.JSONDecodeError):
            pass

        return 100

    
#dynamic input 

name = str(input("Enter Employee Name: "))
l_id = Employee.get_last_employee_id()
print("Last added Employee ID: ",l_id)
emp_id = int(input("Enter Employee ID: "))
if emp_id != l_id + 1:
    raise ValueError(f"Invalid Employee ID! Please enter {l_id + 1}")
salary = int(input("Enter Employee's salary: "))
department = str(input("Enter Employee's department: "))

emp1 = Employee(name, emp_id, salary, department)

emp1.display()
"""
for i in range(0,3):
    n = str(input("You want to see full dataset of all employees ?(yes/no) \n \033[1mNOTE:- The data set you will see is Last Updated\033[0m \n Ans: "))

    if n == "yes" or "Yes" or "Y" or "y":
        AC.API_calling()
        break
    elif n == "no" or "No" or "N" or "n":
        print("Thank you for Add data")
    else:
        print("Enter valid Ans!")
"""