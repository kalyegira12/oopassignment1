import random
class Student:
    def __init__(self, name, reg_number):
        self.name = name
        self.reg_number = reg_number

    def display_details(self):
        print(f"Student Name: {self.name}")
        print(f"Registration Number: {self.reg_number}")

# Example usage:
student1 = Student("Emmanuel Kalyegira", "Reg M23B13/006")
student2 = Student("Jane Smith", "Reg M23B13/001")
student3 = Student("Jordan fanzi", "Reg M23B13/005")
student4 = Student("Nekesa Mercy", "Reg M23B13/008")
student5 = Student("Dominican sir", "Reg M23B13/009")

# Display student details
student1.display_details()
print()  # for separating the output
student2.display_details()
print()
student3.display_details()
print()
student4.display_details()
print()
student5.display_details()
