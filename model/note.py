

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
