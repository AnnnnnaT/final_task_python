from .add_note import Add_note
from .change_note import Change_note
from .delete_note import Delete_note
from .filter_by_date import Filter_by_date
from .show_all import Show_all


class Menu:
    def __init__(self, console):
        self.menu = []
        self.menu.append(Add_note(console))
        self.menu.append(Change_note(console))
        self.menu.append(Delete_note(console))
        self.menu.append(Filter_by_date(console))
        self.menu.append(Show_all(console))

    def show_menu (self):
        title  = "Command's menu:\n"
        for i, elem in enumerate(self.menu, start=1):
            title += f"\t{i}. {elem.description()}\n"
        return title

    def menu_size(self):
        return len(self.menu)

    def to_do(self, num):
        choice = self.menu[num]
        choice.to_do()
        