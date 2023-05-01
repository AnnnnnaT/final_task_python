from abc import ABC, abstractmethod


class Command(ABC):
   
    def __init__(self, console):
        self.console = console

    @abstractmethod
    def description(self):
        """ """

    @abstractmethod
    def to_do(self):
        """ """
