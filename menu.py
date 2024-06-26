import datetime
import time
from model import Model
from output import Output


class Menu:

    def start(self):     
        input("Для входа в программу нажмите Enter")
        model = Model()
        #Output().print_all_notes(model.get_all_notes())
        Menu().first_menu(model)
        
    def enter_menu(self, number_menu):

        while True:
            number_action = input("Ввод: ")
            if number_action.isdigit():
                if number_menu >= int(number_action) > 0:
                    return int(number_action)

    def add_note(self, model):
        title = input("Введите заголовок: ")
        title_body = input("Введите заметку: ")
        time_now = datetime.datetime.today().strftime("%Y-%m-%d/%H.%M.%S")
        separator = ";"
        full_note = title + separator + title_body + separator + time_now
        model.list_add_note(full_note)

    def search_by_date(self, model):
        date = input("Введите дату для поиска заметок (в таком формате: 2001-01-01): ")
        if len(date) != 10:
            return ["Заметок с такой датой нет"]
        list_by_date = model.notes_by_date(date)
        if list_by_date:
            return list_by_date
        else:
            return ["Заметок с такой датой нет"]

    def first_menu(self, model):
        while True:
            print("\n-Главное меню")
            time.sleep(0.1)
            print("Введите 1 для добавления заметки")
            time.sleep(0.1)
            print("Введите 2 для просмотра всех заметок")
            time.sleep(0.1)
            print("Введите 3 для просмотра заметок по дате")
            time.sleep(0.1)
            print("Введите 4 для работы с какой-либо заметкой")
            time.sleep(0.1)
            print("Введите 5 для выхода из программы")

            number_action = Menu().enter_menu(5)
            match number_action:
                case 1:
                    Menu().add_note(model)
                case 2:
                    Output().print_all_notes(model.get_all_notes())
                case 3:
                    Output().print_all_notes(Menu().search_by_date(model))
                case 4:
                    Menu().second_menu(model, Menu().question_menu(model))
                case 5:
                    model.file_write()
                    print("Exit program")
                    return

    def question_menu(self, model):
         while True:
            print("")
            time.sleep(0.3)
            number_note = input("Введите номер заметки с которой вы хотите работать: ")
            if number_note.isdigit():
                if 0 < int(number_note) <= len(model.get_all_notes()):
                    return int(number_note)-1

    def second_menu(self, model, number_note):
         while True:
            print("\n--Меню №2: выбор действия с заметкой номер:", number_note+1)
            time.sleep(0.1)
            print("Введите 1 для редоктирования этой заметки")
            time.sleep(0.1)
            print("Введите 2 для удаления этой заметки")
            time.sleep(0.1)
            print("Введите 3 для просмотра этой заметки")
            time.sleep(0.1)
            print("Введите 4 для возврата в Главное меню")

            number_action = Menu().enter_menu(4)
            match number_action:
                case 1:
                    changed_note = Menu().third_menu(model, number_note)
                    model.change_note(changed_note, number_note)
                case 2:
                    model.del_note(number_note)
                    return
                case 3:
                    print(model.get_one_note(number_note))
                case 4:
                    return

    def third_menu(self, model, number_note):
        note_seporate = model.separate_note(model.get_one_note(number_note))
        
        while True:
            print("\n---Меню №3: редактировать заметку:")
            time.sleep(0.1)
            print("Введите 1 для редоктирования заголовка")
            time.sleep(0.1)
            print("Введите 2 для редоктирования заметки")
            time.sleep(0.1)
            print("Введите 3 для просмотра заметки")
            time.sleep(0.1)
            print("Введите 4 для возврата в меню №2")

            number_action = Menu().enter_menu(4)
            match number_action:
                case 1:
                    print("Заголовок на данный момент:", note_seporate[1])
                    title = input("Введите новый заголовок: ")
                    note_seporate[1] = title
                case 2:
                    print("Заметка на данный момент:", note_seporate[2])
                    note = input("Введите новую заметку: ")
                    note_seporate[2] = note
                case 3:
                    print(note_seporate)
                case 4:
                    note_seporate[3] = datetime.datetime.today().strftime("%Y-%m-%d/%H.%M.%S")
                    return ";".join(note_seporate)

