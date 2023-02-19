f = open("text.in", 'r')
s = f.read()

f.close()
nrtotal = 0
d={}
for c in s:
    if 97 <= ord(c) <= 122:
        nrtotal += 1
        if c in d:
            d[c] +=1
        else:
            d[c] = 1
    elif 65<= ord(c)<= 90:
        nrtotal += 1
        n = ord(c)+32
        if n in d:
            d[chr(n)] += 1
        else:
            d[chr(n)] = 1

for x in d:
    d[x] = d[x]/nrtotal
d = {x: v for x, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}
g = open("text.out", "w")
for i in d:
    g.write(f"{i}: {d[i]: .3f}")
    g.write("\n")
g.close()