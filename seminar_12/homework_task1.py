import csv
import math


class Student:
    def __init__(self, full_name, subjects_file):
        self.full_name = full_name
        self.subjects = self.load_subjects(subjects_file)
        self.grades = {subject: [] for subject in self.subjects}
        self.test_score = {subject: [] for subject in self.subjects}

    def load_subjects(self, subjects_file):
        """Чтение списка предметов"""
        with open(subjects_file, 'r', encoding='utf-8', newline='') as f:
            reader = csv.reader(f)
            subjects = next(reader)
            return subjects

    class NameDescriptor:
        def __init__(self):
            self.value = ''

        def __get__(self, instance, owner):
            return self.value

        def __set__(self, instance, value):
            for name_word in value.split(' '):
                if not (name_word.isalpha() and name_word.istitle()):
                    raise ValueError("ФИО должно начинаться с большой буквы и не содержать цифр: {}".format(value))
            self.value = value

    full_name = NameDescriptor()

    def add_grade(self, subject, grade):
        """"Проверка и хранение оценок по предмету"""
        if subject not in self.subjects:
            raise ValueError(f"Предмет '{subject}' не найден.")
        if not 2 <= grade <= 5:
            raise ValueError("Оценка должна быть в диапазоне от 2 до 5.")
        self.grades[subject].append(grade)

    def add_test_score(self, subject, score):
        """Проверка и сохранение результатов теста по предметам"""
        if subject not in self.subjects:
            raise ValueError(f"Предмет '{subject}' не найден.")
        if not 0 <= score <= 100:
            raise ValueError("Результат теста должен быть в диапазоне от 0 до 100.")
        self.test_score[subject].append(score)

    def average_test_score(self, subject):
        """Выдает результат среднего балла за тесты по предмету"""
        if subject not in self.subjects:
            raise ValueError(f"Предмет '{subject}' не найден.")
        if not self.test_score[subject]:
            raise ValueError("Нет результатов тестов для этого предмета.")
        return f'Средний балл за тесты по предмету {subject}: {round(sum(self.test_score[subject]) / len(self.test_score[subject]), 2)}'

    def average_overall_grade(self):
        """Расчет среднего балла по всем предметам"""
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        if not all_grades:
            raise ValueError("Нет оценок для расчета среднего балла.")
        return f'Средний балл по сумме всех предметов: {round(sum(all_grades) / len(all_grades), 2)}'


student = Student('Николаев Петр Антонович', 'seminars\seminar_12\subjects.csv')

print(student.subjects)
student.add_grade("Русский язык", 5)
student.add_grade("Русский язык", 5)
student.add_test_score("Русский язык", 85)
student.add_test_score("Русский язык", 97)
student.add_grade("Геометрия", 2)
student.add_grade("Геометрия", 3)
student.add_test_score("Геометрия", 27)
student.add_test_score("Геометрия", 47)
student.add_grade("Химия", 4)
student.add_grade("Химия", 5)
student.add_grade("Химия", 5)
student.add_test_score("Химия", 69)
student.add_test_score("Химия", 84)
student.add_test_score("Химия", 79)


print(f'Среднее количество баллов по тестам: {student.average_test_score("Химия")}')
print(f'Средняя оценка всех предметов: {student.average_overall_grade()}')
