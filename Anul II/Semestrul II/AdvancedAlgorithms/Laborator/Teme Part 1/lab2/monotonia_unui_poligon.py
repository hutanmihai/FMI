class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def monotonie(axis: str):
    minimum = float('inf')
    index = 0

    for i in range(n):
        if axis == 'x':
            if points[i].x < minimum:
                minimum = points[i].x
                index = i
        else:
            if points[i].y < minimum:
                minimum = points[i].y
                index = i

    in_crestere = True

    last = points[index].x if axis == 'x' else points[index].y

    for i in range(1, n):
        j = (index + i) % n
        current = points[j].x if axis == 'x' else points[j].y
        
        if current < last:
            in_crestere = False

        if current > last and not in_crestere:
            return False

        last = current

    return True


if __name__ == '__main__':
    monoton_x = True
    monoton_y = True

    n = int(input())
    points = []

    for _ in range(n):
        points.append(Point(*map(int, input().split())))

    monoton_x = monotonie('x')
    monoton_y = monotonie('y')

    if monoton_x:
        print('YES')
    else:
        print('NO')
    if monoton_y:
        print('YES')
    else:
        print('NO')
