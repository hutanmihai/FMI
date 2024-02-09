import sys

f=open(sys.argv[1], 'rb')
h=open(sys.argv[3], 'w')

key=sys.argv[2]
len_key=len(key)

binr=f.read()
binr=binr.decode('utf-8')

text_decriptat=""
n=len(binr)
for i in range(n):
    text_decriptat += chr(ord(binr[i]) ^ ord(key[i % len_key]))

h.write(text_decriptat)

h.close()
f.close()