def bit(x):
    if x // 2 != 0:
        bit(x // 2)
    print(x % 2, end="")

x = input("x = ")
print(x,type(x))
x = int(x)
print(x,type(x))
bit(x)
