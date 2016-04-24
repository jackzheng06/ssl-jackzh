# don't overthink this problem...

input="hsctf{however_this_is_the_real_password}"

#this_isn't_the_real_password}

def password_crypter(password):

    split_password=password.split("_")

    split_password.reverse()

    split_password[3]="isn't"
    split_password[0]=split_password[0][:-1]
    split_password.remove("hsctf{however")

    split_password.reverse()

    new_password=""

    for i in split_password:
        new_password=new_password+i+"_"
    print(new_password[:-1])


password_crypter(input)