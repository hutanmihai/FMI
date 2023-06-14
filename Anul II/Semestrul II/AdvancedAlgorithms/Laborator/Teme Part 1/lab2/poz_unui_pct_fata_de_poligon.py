class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.x < other.x or (self.x == other.x and self.y < other.y)


def output(i):
    if i == 1:
        return "INSIDE"
    elif i == 0:
        return "BOUNDARY"
    elif i == -1:
        return "OUTSIDE"


def sgn(val):
    if val > 0:
        return 1
    elif val < 0:
        return -1
    else:
        return 0


def orientation_test(p1, p2, p3):
    return sgn((p2.x - p1.x) * (p3.y - p1.y) - (p3.x - p1.x) * (p2.y - p1.y))


def is_on_line(p1, p2, p3):
    turn = orientation_test(p1, p2, p3)
    if turn != 0:
        return 0
    if p2.x != p3.x:
        return p2.x <= p1.x <= p3.x or p3.x <= p1.x <= p2.x
    return p2.y <= p1.y <= p3.y or p3.y <= p1.y <= p2.y


def intersection(p1, p2, p3):
    if p1.y > p2.y and p1.y > p3.y:
        return 0
    else:
        if p1.y <= p2.y and p1.y <= p3.y:
            return 0
        else:
            return 1 if float((p1.y - p2.y) * (p3.x - p2.x) + p2.x * (p3.y - p2.y)) / float(p3.y - p2.y) >= p1.x else 0


def get_point_position(polygon, point):
    total_intersections = 0
    for i in range(n - 1):
        if is_on_line(point, polygon[i], polygon[i + 1]):
            return output(0)
        total_intersections += intersection(point, polygon[i], polygon[i + 1])

    if is_on_line(point, polygon[n - 1], polygon[0]):
        return output(0)

    total_intersections += intersection(point, polygon[n - 1], polygon[0])

    if total_intersections % 2 == 1:
        return output(1)
    else:
        return output(-1)


if __name__ == '__main__':
    polygon = []
    points = []

    n = int(input())
    for i in range(n):
        x, y = map(int, input().split())
        polygon.append(Point(x, y))

    m = int(input())
    for i in range(m):
        points.append(Point(*map(int, input().split())))

    for point in points:
        print(get_point_position(polygon, point))
