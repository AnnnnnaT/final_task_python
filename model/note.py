

class Note:

    def __init__(self, title, text, date):
        self.title =title
        self.text = text
        self.date = date
   

    def get_title(self):
        return self.title
    
    def get_text(self):
        return self.text
    
    def get_id(self):
        return self.id
    
    def get_date(self):
        return self.date

    def change(self, title, new_text):
        if title:
            self.title = title
        if new_text:
            self.text = new_text


    # def date_filtered (self, date: str):
    
    #     headers = ['№', 'Заголовок', 'Заметка', 'Дата/время создания', 'Дата/время изменения']
    #     tabl = [[i, note.get_title(), note.get_text_note(), note.get_creation_data(),
    #              note.get_changes_data()] for i, note in enumerate(self.__notes, start=1)
    #             if date in note.get_creation_data() or date in note.get_changes_data()]
    #     return tabulate(tabl, headers=headers, tablefmt="fancy_grid", stralign='center')