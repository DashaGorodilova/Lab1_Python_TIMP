groupmates = [
    {
        "name": "Никита",
        "surname": "Минеев",
        "exams": ["История", "Физика", "Математический анализ"],
        "marks": [4,4,4]

    },

    {
        "name": "Даниил",
        "surname": "Сарачев",
        "exams": ["История", "Физика", "Математический анализ"],
        "marks": [5,3,5]

    },

    {
        "name": "Дмитрий",
        "surname": "Вахтин",
        "exams": ["История", "Физика", "Математический анализ"],
        "marks": [5,4,5]
    },

    {
        "name": "Пётр",
        "surname": "Стрельников",
        "exams": ["История", "Физика", "Математический анализ"],
        "marks": [3,4,3]
    },

    {
        "name": "Ульяна",
        "surname": "Филиппова",
        "exams": ["История", "Физика", "Математический анализ"],
        "marks": [5,5,5]
    },

    {
        "name": "Иван",
        "surname": "Морозов",
        "exams": ["История", "Физика", "Математический анализ"],
        "marks": [3,3,3]
    },

    {
        "name": "Егор",
        "surname": "Маслов",
        "exams": ["История", "Физика", "Математический анализ"],
        "marks": [4,4,3]
    },
]

def filtr(middle, list_of_students):
    lst = []
    for student in list_of_students:
        if sum(student["marks"]) / 3 > middle:
            lst.append(student)
    return lst


def print_students(students):
    print(u"name".ljust(15), u"surname".ljust(10), u"exams".ljust(30), u"marks".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10),
              str(student["exams"]).ljust(30),
              str(student["marks"]).ljust(20))

middle = float(input("Введите средний балл: "))
list_studentov = filtr(middle, groupmates)
print_students(list_studentov)