from .commands.menu import Menu
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
       
        
        print("\nNote is added\n")

    def change_note(self):
                                               
        size = self.presenter.size_notebook()
        id = int(input (f"\nInput note's number to change from 1 to {size} "))
        id = id -1
        new_title = input("\nInput new title for note: ")
        new_text = input("\nInput new text: ")
        self.presenter.change_note(id, new_title, new_text)
        print("\nNote changed!\n")
        

    def show_all(self):
        self.presenter.show_book()
        

    def filtered_book(self):
        date = input("Input filter-date: ")
        print(f"List of notes from {date}\n:", self.presenter.get_filtered_book(date), sep='\n')


    def delete_note(self):      
            self.presenter.size_notebook()
            id = int(input ("\nInput note's number: "))
            self.presenter.remove_note(id)

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
        while self.processing:
            choice = self.id(menu.menu_size(), "\nChoose what to do: ")
            menu.to_do(choice)

    

    
