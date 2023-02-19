def afis_bin(x):
    print(f"{x} = ", end = "")
    binX = bin(abs(x))[2:]
    if binX[0]:
        binX = '0' + binX
    if x >= 0:
        print(binX)
    else:
        print(bin(((2 ** (len(binX)) - 1) ^ abs(x)) + 1)[2:])

a = input("a (bin) = ")
b = input("b (bin) = ")

sum = 0

a = a.strip()

if a[0] == '1':
    sum = -(2 ** (len(a) - 1))

a = a[::-1]

for i in range(len(a) - 1):
    sum += (2 ** i) * int(a[i])

a = sum
sum = 0

b = b.strip()

if b[0] == '1':
    sum = -(2 ** (len(b) - 1))

b = b[::-1]

for i in range(len(b) - 1):
    sum += (2 ** i) * int(b[i])

b = sum


print(f"a = {a}, b = {b}")

if a >= 0 and b > 0:
    val1 = a // b
    val2 = a - b * (a // b)
elif a >= 0 and b < 0:
    cat = a // b
    if a != b * (a // b):
        cat = a // b + 1
    val1 = cat
    val2 = a - (cat * b)
elif a < 0 and b > 0:
    cat = 0
    if a != b * (a // b):
        cat = a // b + 1
    else:
        val1 = a // b
        val2 = 0
        a = b * cat
    if a != b * cat:
        val1 = cat - 1
        val2 = a - ((cat - 1) * b)
else:
    if a < b * (a // b):
         val1 = a // b + 1
         val2 = a - b * (a // b + 1)
    else:
        val1 = a // b
        val2 = 0

print("cat : ", end = "")
afis_bin(val1)
print("rest : ", end = "")
afis_bin(val2)