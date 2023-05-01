from .command import Command

class Change_note(Command):

    def description(self):
        return "Change the note"
    
    def to_do(self):
        self.console.change_note()