from .command import Command

class Filter_by_date(Command):
    def __init__(self, console):
        super().__init__(console)

    def description(self):
        return "Filter notes by date"
    
    def to_do(self):
        self.console.filtered_book(self)