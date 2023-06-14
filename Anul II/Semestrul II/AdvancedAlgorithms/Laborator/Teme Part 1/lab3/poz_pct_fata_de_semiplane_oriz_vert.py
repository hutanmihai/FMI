class Line:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_plane(self, x, y):
        return self.a * x + self.b * y + self.c <= 0


if __name__ == '__main__':
    n = int(input())
    lines = [Line(*map(float, input().split())) for _ in range(n)]

    m = int(input())

    for _ in range(m):
        x, y = map(float, input().split())

        x_low = y_low = float('-inf')
        x_high = y_high = float('inf')

        for line in lines:
            if not line.get_plane(x, y):
                continue

            if line.a == 0:
                cur_y = -line.c / line.b

                if line.b > 0 and cur_y > y:
                    y_high = min(y_high, cur_y)
                elif cur_y < y:
                    y_low = max(y_low, cur_y)

            elif line.b == 0:
                cur_x = -line.c / line.a

                if line.a > 0 and cur_x > x:
                    x_high = min(x_high, cur_x)
                elif cur_x < x:
                    x_low = max(x_low, cur_x)

        print("NO") if (x_high == float('inf') or x_low == float('-inf') or y_high == float('inf') or y_low == float(
            '-inf')) \
            else print(f"YES\n{abs((x_high - x_low) * (y_high - y_low)):.6f}")
