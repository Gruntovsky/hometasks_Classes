class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturers(self, course, grade):
        if course in cool_lecturer.course:
            if grade <= 10:
                cool_lecturer.grades[course] = cool_lecturer.grades.get(course, []) + [grade]
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname,course ):
        super().__init__(name, surname)
        self.course = course
        self.grades = {course: []}

class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print('Оценки за ДЗ:',best_student.grades)

cool_lecturer = Lecturer('Григорий','Грунтовский','Python')
best_student = Student('Александр', 'Иванов', 'Муж')
best_student.rate_lecturers('jawa',10)
best_student.rate_lecturers('Python',8)
best_student.rate_lecturers('Python',10)

print('Студент: ',best_student.name,best_student.surname)
print('Оценки студентов: ',cool_lecturer.grades,'Преподователь: ',cool_lecturer.name,cool_lecturer.surname)

