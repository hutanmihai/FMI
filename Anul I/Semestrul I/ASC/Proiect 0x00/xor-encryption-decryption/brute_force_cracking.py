f=open("outputul_adversarilor", 'rb')
g=open("inputul_adversarilor.txt", 'r')


binr=f.read()
init=g.read()

binr=binr.decode('utf-8')

n=len(init)
index=0
for i in range(n):
    for j in range(128):
        if ord(init[i])^j==ord(binr[i]):
            print(chr(j),end="")
    index+=1
    if index==30:
        break