import csv
from model.note import Note
from model.notebook import Notebook


class Tocsv:

    def __init__(self, path):
        self.path = path

    def write_csv (self, book: Notebook):
        try:
            with open(self.path, 'a', encoding='cp1251', newline='') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow('№', 'Title', 'Note', 'Created')
                for i, note in enumerate(book, start=1):
                        writer.writerow([i, note.get_title(), note.get_text(),
                                        note.get_date()])
        except FileNotFoundError:
               print("Impossible open the file")
    
    def read_csv (self, book:Notebook):
        try:
            with open (self.path,"r", encoding="cp1251") as file:
                reader = csv.reader(file, delimetr = ";")           
                for i, elem in enumerate(reader):
                    if i:
                        book.show_book().append(Note(elem[1], elem[2], elem[3],
                                                        elem[4]))
        except FileNotFoundError:
            pass
        return book



   