n = int(input())

x_low = y_low = float('-inf')
x_high = y_high = float('inf')

for _ in range(n):
    a, b, c = map(float, input().split())

    cur_low = float('-inf')
    cur_high = float('inf')

    if a == 0:
        if b > 0:
            cur_high = -c / b
        else:
            cur_low = -c / b

        y_low = max(y_low, cur_low)
        y_high = min(y_high, cur_high)

    elif b == 0:
        if a > 0:
            cur_high = -c / a
        else:
            cur_low = -c / a

        x_low = max(x_low, cur_low)
        x_high = min(x_high, cur_high)

if x_low > x_high or y_low > y_high:
    print('VOID')
elif x_low == float('inf') or y_low == float('-inf') or x_high == float('-inf') or y_high == float('inf'):
    print('UNBOUNDED')
else:
    print("BOUNDED")
