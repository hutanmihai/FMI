f = open("arce.in", "r")
s = 1
while s:
    s = f.readline().rstrip("\n").split()
    print(s)
    for i in range(len(s)):
        s[0] = [int(x) for x in s[i] if x.isdigit() == True]
    print(s)
# def modifica_arc(d, p1, p2, grosime, culoare):
#     if d[p1]
