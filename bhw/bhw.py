#Bonus Homework
#Noah Schoonover

#------------------------Class Course------------------------
class Course():

    def __init__(self, courseName, courseID, grade, year, semester):
        self.courseName = courseName;
        self.courseID = courseID;
        self.grade = grade;
        self.year = year;
        self.semester = semester;

    def printCourse(self):
        print(
            '{:.<15}{:.>30}\n'
            '{:.<15}{:.>30}\n'
            '{:.<15}{:.>30}\n'
            '{:.<15}{:.>30}\n'
            '{:.<15}{:.>30}\n'.format(
                'Course Name:', self.courseName,
                'Course ID:', self.courseID,
                'Grade:', self.grade,
                'Year:', self.year,
                'Semester:', self.semester)
            )
#------------------------End of Class Course------------------------

#------------------------Class Courses------------------------
class Courses():

    def __init__(self, courses):
        self.courses = courses

    def add(self, course):
        self.courses.append(course)

    def search(self, query):
        try:
            query = int(query)
        except ValueError:
            #search course
            notFound = True
            for course in self.courses:
                if query == course.courseName:
                    course.printCourse()
                    notFound = False
            if notFound:
                print('No courses found with name ' + query)
        else:
            #search year
            notFound = True
            for course in self.courses:
                if query == course.year:
                    course.printCourse()
                    notFound = False
            if notFound:
                print('No courses found for', query)
#------------------------End of Class Courses------------------------
 
#------------------------Test Objects------------------------
#course objects
CSE_101 = Course('Computer Science 101', 'cse_101', 'X', 2018, 'Fall')
MENG_110 = Course('Mechanical Engineering 110', 'meng_110', 'Y', 2018, 'Spring')
MENG_112L = Course('Mechanical Engineering 112 Lab', 'meng_112L', 'Z', 2018, 'Spring')
ENG_101 = Course('English 101', 'eng_101', 'X', 2019, 'Fall')
ENG_104 = Course('English 104', 'eng_104', 'X', 2018, 'Fall')
MATH_114 = Course('Math 114 (Trig)', 'math_101', 'C', 2019, 'Spring')
#courses objects
courses = Courses([CSE_101, MENG_110])
courses.add(MENG_112L)
courses.add(ENG_101)
courses.add(ENG_104)
courses.add(MATH_114)
#------------------------End of Test Objects------------------------
