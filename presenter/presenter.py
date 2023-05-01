from model.tocsv import Tocsv


class Presenter:
    def __init__(self, view, book, path):
        self.view = view
        self.book = book
        self.view.set_presenter(self)
        self.file = Tocsv(path)

    def read_book(self):
        self.book = self.file.read_csv(self.book)

    def add_note(self, title, text):
        self.book.add(title, text)

    def remove_note(self, id: int):
        self.book.remove_note(id)

    def change_note(self, id: int, new_title, new_text):
        self.book.change_note(id, new_title, new_text)
         
    def get_filtered_book(self, date: str):
        return self.book.filter_by_date(date)
    
    def show_book(self):
        return self.book.show_book()  

    def open_csv(self):
        self.book = self.file.read_csv(self.book)

    def save_csv(self):
        self.file.write_csv(self.book)

    def state(self):
        return self.book.state()

   