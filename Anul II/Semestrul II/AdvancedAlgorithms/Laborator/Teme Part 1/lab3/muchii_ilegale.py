class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def numeric_criteria(p1, p2, p3, p4):
    matrix = [
        [p1.x, p1.y, p1.x ** 2 + p1.y ** 2, 1],
        [p2.x, p2.y, p2.x ** 2 + p2.y ** 2, 1],
        [p3.x, p3.y, p3.x ** 2 + p3.y ** 2, 1],
        [p4.x, p4.y, p4.x ** 2 + p4.y ** 2, 1]
    ]

    def det_3x3(m):
        return (
                m[0][0] * m[1][1] * m[2][2]
                + m[0][1] * m[1][2] * m[2][0]
                + m[0][2] * m[1][0] * m[2][1]
                - m[0][2] * m[1][1] * m[2][0]
                - m[0][1] * m[1][0] * m[2][2]
                - m[0][0] * m[1][2] * m[2][1]
        )

    det = (
            matrix[0][0] * det_3x3([
        [matrix[1][1], matrix[1][2], matrix[1][3]],
        [matrix[2][1], matrix[2][2], matrix[2][3]],
        [matrix[3][1], matrix[3][2], matrix[3][3]]
    ])
            - matrix[0][1] * det_3x3([
        [matrix[1][0], matrix[1][2], matrix[1][3]],
        [matrix[2][0], matrix[2][2], matrix[2][3]],
        [matrix[3][0], matrix[3][2], matrix[3][3]]
    ])
            + matrix[0][2] * det_3x3([
        [matrix[1][0], matrix[1][1], matrix[1][3]],
        [matrix[2][0], matrix[2][1], matrix[2][3]],
        [matrix[3][0], matrix[3][1], matrix[3][3]]
    ])
            - matrix[0][3] * det_3x3([
        [matrix[1][0], matrix[1][1], matrix[1][2]],
        [matrix[2][0], matrix[2][1], matrix[2][2]],
        [matrix[3][0], matrix[3][1], matrix[3][2]]
    ])
    )

    if det > 0:
        return "INSIDE"
    elif det < 0:
        return "OUTSIDE"
    else:
        return "BOUNDARY"


def legal_illegal(p1, p2, p3, p4):
    if numeric_criteria(p1, p2, p3, p4) in ["INSIDE", "BOUNDARY"]:
        return "LEGAL"
    else:
        return "ILLEGAL"


if __name__ == '__main__':
    points = []
    for i in range(4):
        points.append(Point(*map(int, input().split())))

    print("AC: ", end="")
    print(legal_illegal(points[1], points[2], points[3], points[0]))
    print("BD: ", end="")
    print(legal_illegal(points[0], points[2], points[3], points[1]))
