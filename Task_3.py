class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.middle_grade = []

    def rate_lecturers(self, course, grade, lecturer):
        if course in lecturer.course:
            if grade <= 10:
                lecturer.grades[course] = lecturer.grades.get(course, []) + [grade]

    def middle_grade_students(self, course):
        middle_grade = round(int(sum(self.grades.get(course))) / len(self.grades.get(course)), 1)
        return middle_grade

    def __str__(self):
        text = f'Student:\nИмя:{self.name}\nФамилия: {self.surname}\nСредняя оценка за ДЗ: {self.middle_grade}' \
               f'\nКурсы в процессе изучения: {",".join(self.courses_in_progress)}' \
               f'\nЗавершенные курсы: {" ".join(self.finished_courses)}'
        return text


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname, course):
        super().__init__(name, surname)
        self.course = course
        self.grades = {course: []}
        self.m_grade = []

    def middle_grade(self, lecturer):
        middle_grade = round(int(sum(lecturer.grades.get(lecturer.course))) / len(lecturer.grades.get(lecturer.course)),
                             1)
        return middle_grade

    def __str__(self):
        text = f'Lecturer:\nИмя:{self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:{self.m_grade}'
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


student1 = Student('Александр', 'Иванов', 'Муж')
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses = ['Java']
student2 = Student('Генадий', 'Покемонов', 'Муж')
student2.courses_in_progress += ['Python', 'Git']
student2.finished_courses = ['Java']

reviewer1 = Reviewer('Аркадий', 'Проверялов')
reviewer1.courses_attached += ['Python']
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student2, 'Python', 10)

reviewer2 = Reviewer('Василий', 'Проверкин')
reviewer2.courses_attached += ['Git']
reviewer2.rate_hw(student1, 'Git', 10)
reviewer2.rate_hw(student2, 'Git', 9)

cool_lecturer1 = Lecturer('Григорий', 'Грунтовский', 'Python')
cool_lecturer2 = Lecturer('Сергей', 'Ильюшин', 'Git')
student1.rate_lecturers('Git', 10, cool_lecturer2)
student1.rate_lecturers('Python', 9, cool_lecturer1)
student2.rate_lecturers('Git', 9, cool_lecturer1)
student2.rate_lecturers('Python', 10, cool_lecturer1)

print(reviewer1)
print()
cool_lecturer1.m_grade.append(cool_lecturer1.middle_grade(cool_lecturer1))
cool_lecturer2.m_grade.append(cool_lecturer2.middle_grade(cool_lecturer2))
print(cool_lecturer1)
print()
student1.middle_grade.append(student1.middle_grade_students('Python'))
student2.middle_grade.append(student2.middle_grade_students('Python'))
print(student1)
print('---------------------')

def compare_lectures():
    if cool_lecturer1.m_grade > cool_lecturer2.m_grade:
         print(f'Лучший лектор:\n {cool_lecturer1}')
    elif cool_lecturer2.m_grade > cool_lecturer1.m_grade:
         print(f'Лучший лектор:\n {cool_lecturer2}')

compare_lectures()

print('--------------------')
def compare_students():
    if student1.middle_grade > student2.middle_grade:
        print(f'Лучший студент:\n {student1}')
    elif student2.middle_grade > student1.middle_grade:
        print(f'Лучший студент:\n {student2}')

compare_students()
