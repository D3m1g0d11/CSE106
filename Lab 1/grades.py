import json

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

class Reader:
    def __init__(self):
        try:
            path = "/Users/John Biton/College Code/CSE S23/CSE 106/Lab 1/"
            with open(path + 'grades.txt', 'r') as file:
                profile = ""
                for lines in file:
                    profile += lines.strip()
            self.grades_dict = json.loads(profile)
            print("Loaded the grades")
        except:
            print("ERROR: Unable to read file")
            raise

    def createStudent(self, name, grade):
        self.grades_dict.update({name : grade})
        print("Student's name: " + name)
        print("Student's grade: " + grade)

    def findStudent(self, name):
        try:
            print(name + " is in the system.\n")     
            return True
        except:
            print("Student is not in the system.\n")
            return False

    def editGrade(self, name, grade):
        if(self.findStudent(name)):
            self.grades_dict[name] = grade
            print(name + "'s new grade is " + grade1)
        else:
            print("Student not found")

    def deleteStudent(self, name):
        if name in self.grades_dict.keys():
            del(self.grades_dict[name])
            print("Deleted Student " + name)
        else:
            print("ERROR: Student not found!")


    def printGrade(self, name):
        try:
            print("Student's name: " + self.grades_dict[name])
            print("Student's grade: " + self.grade)

        except:
            return False

if __name__ == "__main__":
    canvas = Reader()
    while True:
        print("Enter 1 to create a new student")
        print("Enter 2 to find student")
        print("Enter 3 to edit a grade")
        print("Enter 4 to delete a grade")
        print("Enter 5 to print a grade")
        print("Enter 0 to exit\n")
        x = int(input())

        if x == 0:
            break
        elif x == 1:
            name = input("Enter Student's name: ")
            grade = input("Enter " + name + "'s grade: ")
            canvas.createStudent(name, grade)
        elif x not in range(1, 6):
            print("Invalid number")
            continue
        elif x == 2:
            name = input("Enter Student's name to find: ")
            canvas.findStudent(name)
        
        elif x == 3:
            name = input("Enter Student's name to edit a grade: ")
            if(canvas.findStudent(name)):
                newGrade = input("Enter the new grade for " + name + ": ")
                canvas.editGrade(name, newGrade)
            else:
                print("Student is not in the system")
        
        elif x == 4:
            name = input("Enter Student's name to delete: ")
            canvas.deleteStudent(name)        

        elif x == 5:
            for i in canvas.grades_dict.i():
                print("Student: " + i + "\t Grade: " + str(canvas.grades_dict[i]))

    