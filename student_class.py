class student:
    def __init__(self, name, roll_no, age):
        self.roll_no = roll_no
        self.age = age
        self.name = name
    
student1 = student("Jihn", 10, 18)
print(student1.name)
print(student1.roll_no)
print(student1.age)

for i in range(9):
    print(i)