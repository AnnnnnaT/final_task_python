import datetime
from model.note import Note


class Notebook:    

    def __init__(self):
        self.notes = []     

    def add(self, title, text):
        note = Note(title, text, date = datetime.datetime.today())  
        self.notes.append(note)
             
        

    def remove_note(self, id: int):
        self.notes.pop(id)

    def change_note(self, id:int, title, new_text):
        self.notes[id].change(title, new_text)

    def show_book(self):
        return self.notes
    
    def filter_by_date(self, date: str):
        notes = [i, note.get_title(), note.get_text(), note.get_date()]
        for i, note in enumerate(self.notes, start=1):
                if date in note.get_date():
                    return notes[i]
                
    def size(self):
        return len(self.notes)


   