Project: STUDENT PROFILE MANAGER

student = {"name": "Raji",
           "age": 25
            }
print("Student details")
print(student)
print(" "       )
student["age"] = 26
print("Updated details")
print(student)
print("  ")
student["city"] = "Hyderabad"
print("Add new item")
print(student)

---Output:
Student details
{'name': 'Raji', 'age': 25}
 
Updated details
{'name': 'Raji', 'age': 26}
  
Add new item
{'name': 'Raji', 'age': 26, 'city': 'Hyderabad'}

