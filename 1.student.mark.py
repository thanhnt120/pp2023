def inputStudent(numberOfStudent):
    studentList = []  
    for i in range(numberOfStudent):
        print(f"Please enter information of student {i+1}:")
        studentId = input("Enter ID:\n")
        studentName = input("Enter name:\n")
        studentDoB = input("Enter DoB:\n")
        studentInfo = {"ID":studentId,"Name":studentName,"DoB":studentDoB}
        studentList.append(studentInfo)
    return studentList

def inputCourse(numberOfCourse):
    courseList = []  
    for i in range(numberOfCourse):
        print(f"Please enter information of course {i+1}:")
        courseId = input("Enter ID:\n")
        courseName = input("Enter name:\n")
        courseInfo = {"ID":courseId,"Name":courseName}
        courseList.append(courseInfo)
    return courseList

def inputMarks(numberOfStudent):
    markList = []
    for i in range(numberOfStudent):
        print(f"Please enter mark of student {i+1}:")
        mark = input()
        markList.append(mark)
    return markList

numberOfStudent = int(input("Please enter number of students:\n"))
numberOfCourse = int(input("Please enter number of courses:\n"))
studentList = inputStudent(numberOfStudent)
courseList = inputCourse(numberOfCourse)
courseId = input("Select a course to input marks:\n")
isMatch = False
while isMatch == False:
    for i in range(len(courseList)):
        if courseId == courseList[i]["ID"]:
            isMatch = True
            markList = inputMarks(numberOfStudent)
            break
    if isMatch == False:
        courseId = input("Course ID is not in the list. Please select another course:\n")
print(f"Student list: {studentList}")
print(f"Course list: {courseList}")
print(f"Mark list of selected course: {markList}")