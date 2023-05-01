from .command import Command

class Add_note(Command):

    def description(self):
        return "Add new note"

    def to_do(self):
        self.console.add_note()
