import string
import random

def gen():

    str1 = string.ascii_letters
    str2 = string.ascii_uppercase
    str3 = string.ascii_lowercase
    str4 = string.punctuation

    print(str1)
    print(str2)
    print(str3)
    print(str4)

    s = []

    s.extend(list(str1))
    s.extend(list(str2))
    s.extend(list(str3))
    s.extend(list(str4))

    print(s)

    random.shuffle(s)

    password_length = int(input("Enter a length for your password: \n"))

    password = ("".join(s[0:password_length]))

    print(password)

gen()




