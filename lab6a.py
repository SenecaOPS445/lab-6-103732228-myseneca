#!/usr/bin/env python3
# Author ID: 103732228

class Student:
    # Initialize the student object with a name, student number, and an empty dictionary for courses
    def __init__(self, name, number):
        self.name = name
        self.number = str(number)  # Ensure the student number is always a string
        self.courses = {}

    # Return student name and number as a formatted string
    def displayStudent(self):
        return f'Student Name: {self.name}\nStudent Number: {self.number}'

    # Add a new course and grade to the student's record
    def addGrade(self, course, grade):
        self.courses[course] = grade

    # Calculate the grade point average (GPA) of all courses and return a formatted string
    def displayGPA(self):
        if not self.courses:
            return f'GPA of student {self.name} is 0.0'  # Handle case with no courses
        total_grade = sum(self.courses.values())
        GPA = total_grade / len(self.courses) if len(self.courses) > 0 else 0.0
        return f'GPA of student {self.name} is {GPA:.1f}'

    # Return a list of courses that the student passed (grade > 0.0)
    def displayCourses(self):
        passed_courses = [course for course, grade in self.courses.items() if grade > 0.0]
        return passed_courses  # Return the list of passed courses

if __name__ == '__main__':
    # Create first student object and add grades for each class
    student1 = Student('John', 1354900)  # Use integer for student number
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)

    # Create second student object and add grades for each class
    student2 = Student('Jessica', 123456)  # Use integer for student number
    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)

    # Display information for student1 object
    print(student1.displayStudent())
    print(student1.displayGPA())
    print(student1.displayCourses())

    # Display information for student2 object
    print(student2.displayStudent())
    print(student2.displayGPA())
    print(student2.displayCourses())