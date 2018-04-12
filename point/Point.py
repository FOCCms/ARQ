from typing import Type

from point.TextDescription import TextDescription
from point.GPS import GPS
from point.ImageDescription import ImageDescription
import datetime
from point.Label import Label
from abc import abstractmethod


class Point:
    """Базовый класс точки"""

    _isDone = False
    _tipPrice: Type[float]
    _tip = TextDescription()
    _gpsCoordinates = GPS()
    _picture = ImageDescription()
    _startDescription = TextDescription()
    _timeSpentPerforming = datetime
    _capturePrice: float
    _pointLabel = Label()
    _pointType = str


    @abstractmethod
    def goToNextPoint(self):
        pass

