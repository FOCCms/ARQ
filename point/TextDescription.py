from point.PointDescription import PointDescription


class TextDescription(PointDescription):
    """Текстовое описание точки"""
    __text = str()

    def setDescriptionData(self, data):
        self.__text = str(data)

    def getDescriptionData(self):
        return self.__text