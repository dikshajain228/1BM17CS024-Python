import random
import string
def randomStringDigits(stringLength):
    lettersAndDigits = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))
print ("First Random Password is  ", randomStringDigits(10))
