Project: STUDENTS MARKS MANAGER

Program:
marks  =  [80, 90, 95]
print("Original Marks:", marks)
marks.append(100)
print("After adding marks:", marks)
marks.remove(95)
print("After remove marks:", marks)
marks[0] = 85
print("After update marks:", marks)
print("Total number of subjects:", len(marks))

---output:
Original Marks: [80, 90, 95]
After adding marks: [80, 90, 95, 100]
After remove marks: [80, 90, 100]
After update marks: [85, 90, 100]
Total number of subjects: 3




--Final memory sheet
Method	               Purpose
[]	                   Create List
list[index]	           Access Item
append()	             Add Item
remove()	             Remove Item
len()	                 Count Items
list[index] = value	   Update Item
for loop	             Read All Items
