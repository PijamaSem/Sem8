def get_op():
    op = int(input(
        "1 - добавить нового ученика\n2 - добавить новый предмет\n3 - поставить оценку\n"
        "4 - показать оценки ученика\n5 - выход\n"
    ))
    return op

def add_student():
    name = input("Введите Фамилию и Имя ученика: ")
    name = name + " \n"
    with open("students.txt", "a") as file:
        file.write(name)
    print("сохранено!")

def add_subject():
    subject = input("Введите название предмета: ")
    subject = subject + "\n"
    with open("subjects.txt", "a") as file:
        file.write(subject)
    print("сохранено!")