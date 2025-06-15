import random
import string
passlen =12
charpass= string.ascii_letters+string.hexdigits +string.digits
password=""

for i in range(passlen):
      password+=random.choice(charpass)
      
print("Your password is :",password)