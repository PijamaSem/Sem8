def create_jornal():
    # marks = []
    subjects = {}
    # global jornal

    jornal = {}


    with open("students.txt", "r") as file:
        all_names_lines = file.readlines()
        for name in all_names_lines:
            name = name.strip()
            jornal [name] = subjects
            with open("subjects.txt", "r") as file:
                all_lines_s = file.readlines()
                for subjects_name in all_lines_s:
                    subjects_name = subjects_name.strip()
                    subjects[subjects_name] = []

        # print(jornal)
    return(jornal)

def push_mark(student, subject, mark):
    student = student.strip()
    j = create_jornal()
    j[student][subject].append(mark)
    print(j)
