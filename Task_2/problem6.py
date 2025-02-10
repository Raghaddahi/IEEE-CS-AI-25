import random
import string
chars= string.digits + string.ascii_letters
password="".join(random.choices(chars,k=8))
print(f"Generated password is: {password}")
