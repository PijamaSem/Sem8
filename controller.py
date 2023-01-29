import view
import marks
import jornal

def start():
        op = view.get_op()
        while True:
            if op == 1: # Добавить нового ученика
                view.add_student()
            elif op == 2: # Добавить нового предмета
                view.add_subject()
            elif op == 3: # Поставить оценку
                marks.add_mark()
        # elif op == 4: # Показ листа оценок конкретного ученика
            elif op == 5:
                break