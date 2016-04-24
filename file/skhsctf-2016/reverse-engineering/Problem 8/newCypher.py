entry=input()

def passwordChecker(password):
    i=int(password,35);
    i=i**0.5
    return (i==1209389)

print(passwordChecker(entry));