import os


class File:
    NAME_FILE: str = "Notes.csv"

    def read_file(self):
        all_notes = []

        # os.path.exists(NAME_FILE) - проверяет существует ли файл
        if os.path.exists(self.NAME_FILE):
        # with open(NAME_FILE) as f: - Открывает файл для чтения и он автоматически закрывается потом.
            with open(self.NAME_FILE) as f:
                for line in f.read().splitlines():
                    all_notes.append(line)
                print("Get data from notes file")
        #else:
            #with open(self.NAME_FILE, "w") as f:
                #pass
        return all_notes

    def write(self, all_notes):
        with open(self.NAME_FILE, "w") as f:
            for note in all_notes:
                f.writelines(f"{note}\n")


