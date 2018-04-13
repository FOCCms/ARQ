from abc import abstractmethod


class Label:
    """Базовый класс меток"""

    @abstractmethod
    def getLabel(self):
        pass

    @abstractmethod
    def setLabel(self, label):
        pass

    @abstractmethod
    def checkLabel(self):
        pass
