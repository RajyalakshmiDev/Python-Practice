project : # Student Result Checker

name = input("Enter student name: ")
marks = int(input("Enter marks: "))

print("Hello", name)

if marks >= 90:
    print("Grade: A")
    print("Excellent")
elif marks >= 75:
    print("Grade: B")
    print("Very Good")
elif marks >= 50:
    print("Grade: C")
    print("Pass")
else:
    print("Grade: Fail")
    print("Better Luck Next Time")

---Output:
Enter student name: Raji
Enter marks: 95
Hello RAji
Grade A
Excellent
