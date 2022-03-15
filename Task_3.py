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

    def middle_grade_students(self):
        middle_grade = round(int(sum(best_student.grades.get(cool_lecturer.course)))/len(best_student.grades.get(cool_lecturer.course)),1)
        return middle_grade

    def __str__(self):
        text = f'Student:\nИмя:{self.name}\nФамилия: {self.surname}\nСредняя оценка за ДЗ:{self.middle_grade_students()},' \
               f'\nЗавершенные курсы: {" ".join(self.finished_courses)}'
        return text

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

    def middle_grade(self):
        middle_grade = round(int(sum(cool_lecturer.grades.get(cool_lecturer.course)))/len(cool_lecturer.grades.get(cool_lecturer.course)),1)
        return middle_grade

    def __str__(self):
        text = f'Lecturer:\nИмя:{self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:{self.middle_grade()}'
        return text

class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        text = f'Reviewer:\nИмя:{self.name}\nФамилия: {self.surname}'
        return text

best_student = Student('Александр', 'Иванов', 'Муж')
best_student.courses_in_progress += ['Python','Git']
best_student.finished_courses = ['Java']

cool_mentor = Reviewer('Аркадий', 'Проверялов')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 9)
cool_mentor.rate_hw(best_student, 'Python', 10)

cool_lecturer = Lecturer('Григорий','Грунтовский','Python',)
best_student.rate_lecturers('Git',10)
best_student.rate_lecturers('Python',9)
best_student.rate_lecturers('Python',10)
best_student.rate_lecturers('Python',10)
best_student.rate_lecturers('Python',10)

print(cool_mentor)
print()
print(cool_lecturer)
print()
print(best_student)