w = input("w=")
p = int(input("p="))
n = int(input("n="))
sir = ""

sufw = w[-p:]
for i in range (n):
    s= input()
    if len(s)-p >= 2 and s[-p:] == sufw:
        sir += s + " "
print (sir)

# s = input("s=")
# print (s.split())
