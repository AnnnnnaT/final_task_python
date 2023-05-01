from .command import Command

class Show_all(Command):
    
    def description(self):
        return "Show all notes in notebook"
    
    def to_do(self):
        self.console.show_all()