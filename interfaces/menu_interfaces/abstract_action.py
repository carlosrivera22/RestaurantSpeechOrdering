import abc

class AbstractAction(abc.ABC):
    @abc.abstractmethod
    def execute(self,arg):
        pass

