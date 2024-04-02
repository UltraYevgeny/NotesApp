import os


class File:
    # ВАЖНО!!!!
    # Для коректной работы файл Notes.csv - должен находиться в каталоге
    NAME_FILE: str = "Notes.csv"

    def read_file(self):
        all_notes = []

        if os.path.exists(self.NAME_FILE):
            with open(self.NAME_FILE) as f:
                for line in f.read().splitlines():
                    all_notes.append(line)
        return all_notes

    def write(self, all_notes):
        with open(self.NAME_FILE, "w") as f:
            for note in all_notes:
                f.writelines(f"{note}\n")


