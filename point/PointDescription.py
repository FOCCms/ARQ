from abc import abstractmethod


class PointDescription:
    """Базовый класс описания точки"""

    @abstractmethod
    def getDescriptionData(self):
        pass

    @abstractmethod
    def setDescriptionData(self, data):
        pass

