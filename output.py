import time
class Output:

    def print_all_notes(self, notes):
        print("\nСписок заметок:")
        for note in notes:
            time.sleep(0.3)
            print(note)

