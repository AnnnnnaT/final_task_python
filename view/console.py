from view.commands.menu import Menu
from .view import View

class Console(View):

    processing = False
    save = True
    start = False

    def __init__(self):
        self.presenter = None

    def set_presenter(self, presenter):
        self.presenter = presenter

    def add_note(self):    
        title = input("\nInput title of the note: ")
        text = input("\nInput text: ")
        self.presenter.add_note(title, text)
        self.save = False         
        print("\nNote is added\n")

    def change_note(self):
                                               
        size = self.presenter.size_notebook()
        id = int(input (f"\nInput note's number to edit from 1 to {size} "))
        id = id -1
        new_title = input("\nInput new title for note: ")
        new_text = input("\nInput new text: ")
        self.presenter.change_note(id, new_title, new_text)
        print("\nNote edited!\n")
        

    def show_all(self):
        if self.presenter.state():
            print("\nExsisting notes")
            self.presenter.show_book()
        else:
            print("\nNo notes yet")


    def filtered_book(self):
        if self.presenter.state():
            date = input("Input filter-date: ")
            print(f"List of notes from {date}\n:", self.presenter.get_filtered_book(date), sep='\n')
        else:
            print("\nNo notes yet")

    def delete_note(self):    
            if self.presenter.state():  
                choice = self.id (self.presenter.size_notebook(), "\nChoose note by it's number: ")
                self.presenter.remove_note(choice)
            else:
                print("\nNo notes yet")

    
    def save_work(self):
        if not self.start:
            user = input("Save edits?: ")
            if user.lower() == 'yes':
                self.presenter.save()
                self.save = True
                print("\nDone!")
        else:
            self.presenter.save()
            self.save = True
            print("\nDone!")

    def id(size: int, text):
            while True:
                user_enter = input(text)
                if (user_enter.isdigit() and
                        1 <= int(user_enter) <= size):
                    id = int(user_enter) - 1
                    return id
                print(f"\nInput number from 1 to {size}")    

    def start_work(self):
        self.processing = True
        menu = Menu(self)
        print(menu)       
        size = menu.menu_size()
        text = "\nChoose what to do:"
        while self.processing:
            choice = self.id(size, text)
            menu.to_do(choice)

   
   

    def start_notebook(self):
        if self.start:
            self.presenter.open_csv()
            self.open = True
            if self.presenter.state():
                print("\nLet's start")
            else:
                print("\nNo notes yet")  
   

    def stop(self):
        if self.save:
            self.processing = False 
            return
        user = input("\Save edits? ").lower()

        if user == 'yes' and self.start:
            self.presenter.save()
            self.save = True
            print("\nDone!")
        self.pricessing = False
        print("\nENd of work")



  