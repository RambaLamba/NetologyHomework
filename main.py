class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        avg_grade = self.average_grade()
        courses_in_progress = ", ".join(self.courses_in_progress)
        finished_courses = ", ".join(self.finished_courses)
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade}\n"
                f"Курсы в процессе изучения: {courses_in_progress}\n"
                f"Завершенные курсы: {finished_courses}")

    def average_grade(self):
        total = 0
        count = 0
        for grades in self.grades.values():
            total += sum(grades)
            count += len(grades)
        return round(total / count, 1) if count > 0 else 0

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Можно сравнивать только студентов между собой")
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Можно сравнивать только студентов между собой")
        return self.average_grade() <= other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Можно сравнивать только студентов между собой")
        return self.average_grade() == other.average_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Можно сравнивать только студентов между собой")
        return self.average_grade() > other.average_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}  # переименовано из grades_students для единообразия

    def __str__(self):
        avg_grade = self.average_grade_students()
        return f"{super().__str__()}\nСредняя оценка за лекции: {avg_grade}"

    def average_grade_students(self):
        total = 0
        count = 0
        for grades in self.grades.values():
            total += sum(grades)
            count += len(grades)
        return round(total / count, 1) if count > 0 else 0

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Можно сравнивать только лекторов между собой")
        return self.average_grade_students() < other.average_grade_students()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Можно сравнивать только лекторов между собой")
        return self.average_grade_students() <= other.average_grade_students()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Можно сравнивать только лекторов между собой")
        return self.average_grade_students() == other.average_grade_students()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Можно сравнивать только лекторов между собой")
        return self.average_grade_students() > other.average_grade_students()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

# Функция для подсчета средней оценки за домашние задания студентов конкретного курса
def calculate_avg_hw_grade(students, course):
    total = 0
    count = 0
    for student in students:
        if course in student.grades:
            total += sum(student.grades[course])
            count += len(student.grades[course])
    return round(total / count, 1) if count > 0 else 0

# Функция для подсчета средней оценки лекторов конкретного курса
def calculate_avg_lecture_grade(lecturers, course):
    total = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    return round(total / count, 1) if count > 0 else 0

# Сравнение студентов по средней оценке.
def compare_students(first_student, second_student):
    if first_student > second_student:
        print("Первый студент учится лучше!")
    elif first_student < second_student:
        print("Второй студент учится лучше!")
    else:
        print("Студенты имеют одинаковый средний балл!")

# Сравнение лекторов по средней оценке.
def compare_lecturer(first_lecturer, second_lecturer):
    if first_lecturer > second_lecturer:
        print("У первого лектора рейтинг выше!")
    elif first_lecturer < second_lecturer:
        print("У второго лектора рейтинг выше!")
    else:
        print("Лекторы имеют одинаковый рейтинг!")

# ПОЛЕВЫЕ ИСПЫТАНИЯ!!!
# Студенты
student1 = Student("Николай", "Ильинский", "мужской")
student1.courses_in_progress = ["Python", "Git"]
student1.finished_courses = ["Введение в программирование"]

student2 = Student("Галина", "Воронина", "женский")
student2.courses_in_progress = ["Python"]
student2.finished_courses = ["Git"]

# Лекторы
lecturer1 = Lecturer("Олег", "Темирбаев")
lecturer1.courses_attached = ["Python"]
lecturer2 = Lecturer("Татьяна", "Буланова")
lecturer2.courses_attached = ["Git", "Python"]

# Проверяющие
reviewer1 = Reviewer("Виктор", "Цой")
reviewer1.courses_attached = ["Python"]
reviewer2 = Reviewer("Алла", "Пугачёва")
reviewer2.courses_attached = ["Git"]

# Проверяющие выставляют оценки студентам
reviewer1.rate_hw(student1, "Python", 9)
reviewer1.rate_hw(student1, "Python", 10)
reviewer1.rate_hw(student2, "Python", 8)

reviewer2.rate_hw(student1, "Git", 7)
reviewer2.rate_hw(student1, "Git", 9)

# Студенты выставляют оценки лекторам
student1.rate_lecturer(lecturer1, "Python", 6)
student1.rate_lecturer(lecturer1, "Python", 7)
student2.rate_lecturer(lecturer1, "Python", 8)

student1.rate_lecturer(lecturer2, "Git", 7)
student1.rate_lecturer(lecturer2, "Git", 9)
student1.rate_lecturer(lecturer2, "Python", 8)

print("Информация о студентах:")
print()
print(student1)
print()
print(student2)
print("\n" + "="*50 + "\n")

print("Информация о лекторах:")
print()
print(lecturer1)
print()
print(lecturer2)
print("\n" + "="*50 + "\n")

print("Информация о проверяющих:")
print()
print(reviewer1)
print()
print(reviewer2)
print("\n" + "="*50 + "\n")

# Сравнение студентов
print("Сравнение студентов:")
compare_students(student1, student2)
print("\n" + "="*50 + "\n")

# Сравнение лекторов
print("Сравнение лекторов:")
compare_lecturer(lecturer1, lecturer2)
print("\n" + "="*50 + "\n")

# Используем функции для подсчета средних оценок
students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]

print("Средние оценки по курсам:")
print(f"Средняя оценка за домашние задания по курсу Python: {calculate_avg_hw_grade(students_list, 'Python')}")
print(f"Средняя оценка за лекции по курсу Python: {calculate_avg_lecture_grade(lecturers_list, 'Python')}")
print(f"Средняя оценка за лекции по курсу Git: {calculate_avg_lecture_grade(lecturers_list, 'Git')}")
print("\n" + "="*50 + "\n")
