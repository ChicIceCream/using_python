class Student:
    def __init__(self, name, roll_no, age):
        self.roll_no = roll_no
        self.age = age
        self.name = name
    
Student1 = Student("Jihn", 10, 18)
print(Student1.name)
print(Student1.roll_no)
print(Student1.age)

for i in range(9):
    print(i)