from typing import Type

from point.TextDescription import TextDescription
from point.GPS import GPS
from point.ImageDescription import ImageDescription
import datetime
from point.Label import Label
from abc import abstractmethod


class Point:
    """Базовый класс точки"""

    def __init__(self, type: str, label: Label, gps: GPS, startDescription: TextDescription,
                 image: ImageDescription, price: float, tip: TextDescription, tipPrice: float):
        self._pointType = type
        self._pointLabel = Label().setLabel(label)
        self._gpsCoordinates = GPS().setDescriptionData(gps)
        self._startDescription = TextDescription().setDescriptionData(startDescription)
        self._picture = ImageDescription().setDescriptionData(image)
        self._capturePrice = price

        self._tip = TextDescription().setDescriptionData(tip)
        self._tipPrice = tipPrice
        self._timeSpentPerforming: datetime
        self._isDone = False

    @abstractmethod
    def goToNextPoint(self):
        pass

