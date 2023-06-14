class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False


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


def binary_search(polygon, point):
    left = 0
    right = len(polygon) - 1
    while left <= right:
        mid = (left + right) // 2
        turn = orientation_test(polygon[0], polygon[mid], point)
        if turn > 0:
            left = mid + 1
        elif turn < 0:
            right = mid - 1
        else:
            return mid
    return right


def get_point_position(polygon, point):
    n = len(polygon)
    i = binary_search(polygon, point)

    if i == 0:
        return output(-1)

    if orientation_test(polygon[i - 1], polygon[i], point) == 0:
        if min(polygon[i - 1].x, polygon[i].x) <= point.x <= max(polygon[i - 1].x, polygon[i].x) \
                and min(polygon[i - 1].y, polygon[i].y) <= point.y <= max(polygon[i - 1].y, polygon[i].y):
            return output(0)
        else:
            return output(-1)

    return output(sgn(orientation_test(polygon[i], polygon[(i + 1) % n], point)))


if __name__ == '__main__':
    check = {}
    polygon = []
    points = []

    with open('convex4.in') as f:
        n = int(f.readline())
        for i in range(n):
            x, y = map(int, f.readline().split())
            polygon.append(Point(x, y))
            check[Point(x, y)] = True

        m = int(f.readline())
        for i in range(m):
            points.append(Point(*map(int, f.readline().split())))

    for point in points:
        if point in check.keys():
            print(output(0))
        else:
            print(get_point_position(polygon, point))

    # n = int(input())
    # for i in range(n):
    #     x, y = map(int, input().split())
    #     polygon.append(Point(x, y))
    #     check[Point(x, y)] = True
    #
    # m = int(input())
    # for i in range(m):
    #     points.append(Point(*map(int, input().split())))
    #
    # for point in points:
    #     if point in check.keys():
    #         print(output(0))
    #     else:
    #         print(get_point_position(polygon, point))
