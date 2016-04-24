from passlib.hash import sha256_crypt

entry=input()

passwordfile=open("passwordfile.txt")

def passwordEncrypter(password):
    h = sha256_crypt.encrypt(password)
    return (passwordfile==h)

print(passwordChecker(entry));