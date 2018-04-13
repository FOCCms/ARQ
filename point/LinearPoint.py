from point.Point import Point


class LinearPoint(Point):
    """Линейная точка. Без ветвлений"""

    def __init__(self, type, label, gps, startDescription, image, price, tip, tipPrice):
        super().__init__(type, label, gps, startDescription, image, price, tip, tipPrice)