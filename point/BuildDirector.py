from point.LinearPointBuilder import LinearPointBuilder

class BuildDirector(object):
    @staticmethod
    def construct_linear_point():
        builder = LinearPointBuilder()
        builder.set_type(type)
        builder.set_lable(label)
        builder.set_gps(gps)
        builder.set_start_description(start_description)
        builder.set_image(image)
        builder.set_price(price)
        builder.set_tip(tip)
        builder.set_tipPrice(tipPrice)
        return builder.get_result()