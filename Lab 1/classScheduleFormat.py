import string

class course:
        def __init__(self, subj, num, name, units, days, start, end, ave):
            self.subj = subj
            self.classNum = num
            self.className = name
            self.classUnits = units
            self.classDays = days
            self.classStart = start
            self.classEnd = end
            self.classAve = ave

        def printSchedule(self, count):
            lineOne = "COURSE " + str(count) +  ": {department}{number} {name} \n"     
            print(lineOne.format(department = self.subj, number = self.classNum, name = self.className))
            lineTwo = "Number of Credits: {credits}\n" 
            print(lineTwo.format(credits = self.classUnits))
            lineThree = "Days of Lectures: {days}\n" 
            print(lineThree.format(days = self.classDays))
            lineFour = "Lecture Time:  {start} - {end}\n" 
            print(lineFour.format(start = self.classStart, end = self.classEnd))
            lineFive = "Stat: on average, students get {average}% in this course\n"
            print(lineFive.format(average = self.classAve))
def classScheduleFormat():
    #Change path here
    path = "/Users/John Biton/College Code/CSE S23/CSE 106/Lab 1/"
    with open(path + 'classesInput.txt', 'r') as file:
        #Takes in the number of courses in the text file
        count = int(file.readline())
        #Reads each line in the text file and places them in the parameter
        for i in range(1, count):
            d = course(file.readline().strip(), file.readline().strip(), file.readline().strip(), file.readline().strip(), file.readline().strip(), file.readline().strip(), file.readline().strip(), file.readline().strip())
            d.printSchedule(i)
            
    file.close()

if __name__ == "__main__":
    classScheduleFormat()