import sys

key=sys.argv[1]
f=open(sys.argv[2], 'r')
g=open(sys.argv[3], 'w')

len_key=len(key)

s=f.read()
text_criptat = ""

for i in range(len(s)):
    sir=chr(ord(s[i]) ^ ord(key[i%len_key]))
    text_criptat+=sir

text_criptat=bytes(text_criptat.encode('utf-8'))

g.write(text_criptat)

g.close()
f.close()