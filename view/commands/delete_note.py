from .command import Command

class Delete_note(Command):

    def description(self):
        return "Delete note"
    
    def to_do(self):
        self.console.delete_note()