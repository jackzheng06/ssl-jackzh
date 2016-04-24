flag=input()

encodedFlag=""
for c in flag:
    k=((ord(c)+12))
    if k>122 or (k>90 and k<102):
        k=k-26
    encodedFlag+=chr(k)
print("hsctf{"+encodedFlag+"}")