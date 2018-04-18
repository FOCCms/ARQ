from abc import abstractmethod
from abc import ABCMeta


class Builder:
    __metaclass__ = ABCMeta

    @abstractmethod
    def set_type(self, value: str):
        pass

    @abstractmethod
    def set_lable(self, value: Label):
        pass

    @abstractmethod
    def set_gps(self, value : GPS):
        pass

    @abstractmethod
    def set_start_description(self, value: TextDescription):
        pass

    @abstractmethod
    def set_image(self, value: ImageDescription):
        pass

    @abstractmethod
    def set_price(self, value: float):
        pass

    @abstractmethod
    def set_tip(self, value: TextDescription):
        pass

    @abstractmethod
    def set_tipPrice(self, value: float):
        pass

    @abstractmethod
    def get_result(self):
        pass