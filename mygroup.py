groupmates = [
    {
        "name": "Яна",
        "surname": "Лунёва",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Анастасия",
        "surname": "Гальцова",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Александр",
        "surname": "Яньшин",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    }
]


def search_middle():
    search = float(input("средняя оценка"))
    new_group = []
    for students in groupmates:
        middle = sum(students['marks']) / len(students['marks'])
        if middle >= search:
            students['middle'] = middle
            new_group.append(students)
    print_students(new_group)


def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(43), u"Оценки".ljust(20),
          u"средняя оценка".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(40),
              str(student["marks"]).ljust(25), str(student["middle"]).ljust(30))


search_middle()
