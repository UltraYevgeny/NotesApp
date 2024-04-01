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
       
    def del_note(self, number_note):
        del self.all_notes[number_note]
        print("Заметка удалена")

    def file_write(self):
        File().write(self.all_notes)

    def separate_note(self, note):
        separate_note = []
        for part in note.split(";"):
            separate_note.append(part)
        return separate_note



