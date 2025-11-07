#!/usr/bin/env python3
# Author ID: Vaidehi - vpatel278 - 166249219

class Student:

    # Define the name and number when a student object is created, ex. student1 = Student('john', 25969102)
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.courses = {}

    # Return student name and number
    # must NOT fail if self.number is an int
    def displayStudent(self):
        return 'Student Name: ' + self.name + '\n' + 'Student Number: ' + str(self.number)

    # Add a new course and grade to students record
    def addGrade(self, course, grade):
        self.courses[course] = grade

    # Calculate the grade point average of all courses and return a string
    # must handle divide-by-zero cleanly
    def displayGPA(self):
        # no courses at all
        if len(self.courses) == 0:
            return 'GPA of student ' + self.name + ' is 0.0'

        total = 0.0
        for course in self.courses.keys():
            total = total + self.courses[course]

        # if all grades are 0.0, still return 0.0
        if total == 0.0:
            gpa = 0.0
        else:
            gpa = total / len(self.courses)

        return 'GPA of student ' + self.name + ' is ' + str(gpa)

    # Return a list of courses that the student passed (not a 0.0 grade)
    def displayCourses(self):
        passed = []
        for course, grade in self.courses.items():
            if grade != 0.0:
                passed.append(course)
        return passed


if __name__ == '__main__':
    # Create first student object and add grades for each class
    student1 = Student('John', '013454900')
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)

    # Create second student object and add grades for each class
    # NOTE: number is an INT here on purpose to test displayStudent()
    student2 = Student('Jessica', 123456)
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

