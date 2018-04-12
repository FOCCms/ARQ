from point.Point import Point
from point.LinearPoint import LinearPoint

class Quest(Point):
    """Сам квест"""

    pointArray = []
    for i in range(6):
        lp = LinearPoint()
        lp._tipPrice = i
        pointArray.append(lp)


if __name__ == '__main__':
    q = Quest()
    for point in q.pointArray:
        print(point._tipPrice)
