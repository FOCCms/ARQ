from point.Builder import Builder
from point.LinearPoint import LinearPoint


class LinearPointBuilder(Builder):

    def __init__(self):
        self.LinearPoint = LinearPoint()

    def set_type(self, value: str):
        self.LinearPoint._pointType = value

    def set_lable(self, value: Label):
        self.Linearpoint._pointLabel = value

    def set_gps(self, value : GPS):
        self.LinearPoint._gpsCoordinates = value

    def set_start_description(self, value: TextDescription):
        self.LinearPoint._startDescription = value

    def set_image(self, value: ImageDescription):
        self.LinearPoint._picture = value

    def set_price(self, value: float):
        self.LinearPoint._capturePrice = value

    def set_tip(self, value: TextDescription):
        self.LinearPoint._tip = value

    def set_tipPrice(self, value: float):
        self.LinearPoint._tipPrice = value

    def get_result(self):
        return self.LinearPoint
