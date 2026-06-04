--- Def: A dictionary stores data in key-value pairs.

---Creating Dictionary
student = {"name": "Raji", 
           "age": 25,
           "city": "Hyderabad"
           }
print(student)

---output:
{'name': 'Raji', 'age': 25, 'city': 'Hyderabad'}
---------------------------------------------------------------------------------------------------------

----Access Value : A value can be accessed using its key

Example:
student = {"name": "Raji", 
           "age": 25,
           "city": "Hyderabad"
           }
print(student["name")

--Output:
Raji
---------------------------------------------------------------------------------------------------------
--- Update Value: An existing value can be updated using its key

student = {"name": "Raji", 
           "age": 25,
           }
student["age"] = 26
print(student)

---Output:
{'name': 'Raji', 'age': 26}
---------------------------------------------------------------------------------------------------------

---Add New Item: Item can be add in a list.

student = {"name": "Raji"}
student["city"] = "Hyderabad"
print(student)

--Output:
{'name': 'Raji', 'city': 'Hyderabad'}
---------------------------------------------------------------------------------------------------------
