from passlib.hash import sha256_crypt

entry=input()

newpassword=open("passwordstorage.txt")

def passwordEncrypter(password):
    h = sha256_crypt.encrypt(password+"kj2bd28hda23")
    return (newpassword==h)

print(passwordChecker(entry));