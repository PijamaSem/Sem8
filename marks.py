import jornal

def add_mark():
    while True:
        print("Выберите ученика для установки оценки: ")
        print("Для выхода нажмите 'q'")
        with open("students.txt","r") as file:
            all_lines = file.readlines()
            for indx,val in enumerate(all_lines):
                print(indx, all_lines[indx].strip())
            num_student = input()
            if num_student == 'q':
                break
            elif num_student.isdigit():
                print (all_lines[int(num_student)])
                print("Выберите предмет: ")
                print("Для выхода нажмите 'q'")
                with open("subjects.txt", "r") as file:
                    all_lines_s = file.readlines()
                    for indx, val in enumerate(all_lines_s):
                        print(indx, all_lines_s[indx].strip())
                    num_subject = (input())
                    if num_subject == 'q':
                        break
                    elif num_subject.isdigit():
                        print(all_lines_s[int(num_subject)])
                        mark = int(input("Введите оценку:"))
                        # print(all_lines[int(num_student)],all_lines_s[indx].strip(),mark)
                        print(jornal)
                        jornal.push_mark(all_lines[int(num_student)], all_lines_s[indx].strip(), mark)


