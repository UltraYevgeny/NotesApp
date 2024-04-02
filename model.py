from file import File


class Model:
    all_notes: list

    def __init__(self):
        self.all_notes = File().read_file()
    
    def get_all_notes(self):
        return self.all_notes
    
    def get_one_note(self, number_note):
        return self.all_notes[number_note]
    
    def list_add_note(self, note):
        number = str(len(self.all_notes) + 1)
        self.all_notes.append(number + ";" + note)
        print("Заметка добавлена")
       
    def del_note(self, number_note):
        del self.all_notes[number_note]
        count = 0
        for note in self.all_notes:
            count += 1
            number, title, title_body, time_this = note.split(";")
            number = str(count)
            separator = ";"
            full_note = number + separator + title + separator + title_body + separator + time_this
            self.all_notes[count-1] = full_note
        print("Заметка удалена")

    def file_write(self):
        File().write(self.all_notes)
        print("Данные сохранены в файл")

    def separate_note(self, note):
        separate_note = []
        for part in note.split(";"):
            separate_note.append(part)
        return separate_note

    def change_note(self, changed_note, number_note):
        self.all_notes[number_note] = changed_note
        print("Заметка изменина")

    def notes_by_date(self, date):
        filtered_list = []
        for note in self.all_notes:
            count = 0
            for part in note.split(";"):
                count += 1
                if count == 4:
                    for date_part in part.split("/"):
                        if date_part == date:
                            filtered_list.append(note)
        return filtered_list


