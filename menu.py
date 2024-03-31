import datetime
import time
from model import Model
from output import Output


class Menu:

    def start(self):     
        input("Для входа в программу нажмите Enter")
        model = Model()
        Output().print_all_notes(model.get_all_notes())
        
        Menu().first_menu(model)

    def enter_menu(self, number_menu):
        while True:
            number_action = int(input("Ввод: "))
            if number_action <= number_menu:
                return number_action

    def add_note(self, model):
        title = input("Введите заголовок: ")
        title_body = input("Введите заметку: ")
        time = datetime.datetime.today().strftime("%Y-%m-%d / %H.%M.%S")
        separator = ";"
        full_note = title + separator + title_body + separator + time
        model.list_add_note(full_note)

    def first_menu(self, model):
        while True:
            print("")
            time.sleep(0.3)
            print("Введите 1 для добавления заметки")
            time.sleep(0.3)
            print("Введите 2 для просмотра всех заметок")
            time.sleep(0.3)
            print("Введите 3 для работы с какой-либо заметкой")
            time.sleep(0.3)
            print("Введите 4 для выхода из программы")
            
            number_action = Menu().enter_menu(4)
            match number_action:
                case 1:
                    Menu().add_note(model)
                case 2:
                    Output().print_all_notes(model.get_all_notes())
                case 3:
                    Menu().second_menu(model, Menu().question_menu(model))
                case 4:
                    print("Exit")
                    return

    def question_menu(self, model):
         while True:
            print("")
            time.sleep(0.3)
            number_note = int(input("Введите номер заметки с которой вы хотите работать: "))
            if number_note <= len(model.get_all_notes()):
                return number_note-1

    def second_menu(self, model, number_note):
         while True:
            print("")
            time.sleep(0.3)
            print("Введите 1 для редоктирования этой заметки")
            time.sleep(0.3)
            print("Введите 2 для удаления этой заметки")
            time.sleep(0.3)
            print("Введите 3 для просмотра этой заметки")
            time.sleep(0.3)
            print("Введите 4 для возврата в предыдущее меню")

            number_action = Menu().enter_menu(4)
            match number_action:
                case 1:
                    Menu().third_menu(model, number_note)
                case 2:
                    model.del_note(number_note)
                    return
                case 3:
                    print(model.get_one_note(number_note))
                case 4:
                    return

    def third_menu(self, model, number_note):
        return






