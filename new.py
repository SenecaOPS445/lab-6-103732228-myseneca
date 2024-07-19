#!/usr/bin/env python3

from student import Student
# Creates an instance of the Student class, it will be separate from all other objects created with the Student class:
student1 = Student('John', '013454900')
student2 = Student('Jessica', '023384103')

# Add new courses for student1
student1.addGrade('uli101', 4.0)
student1.addGrade('ops245', 3.5)
student1.addGrade('ops445', 3.0)

# Add new courses for student2
student2.addGrade('ipc144', 4.0)
student2.addGrade('cpp244', 4.0)


# student1.name is a string like any other
print(student1.name)
student1.name = 'Jack'
print(student1.name)
print(len(student1.name))

def __init__(self, name, number):
    self.name = name
    self.number = number
    self.courses = {}