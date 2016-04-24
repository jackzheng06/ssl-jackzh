# don't overthink this problem...

input="elevendigit"

def password_decrypter(password):
    changed=changer(password)
    weird=wierder(changed)
    print (weird)
def changer(q):
    altered_password=""
    for c in q: altered_password+=chr(ord(c)*2)
    return altered_password
def wierder(l):
    o=""
    cu=-1
    c=[98,101,103,120,100,97,99,113,91,89,107]
    for h in l:
        cu+=1
        o+=chr((ord(h)-c[cu]))
    return(o)

password_decrypter(input)