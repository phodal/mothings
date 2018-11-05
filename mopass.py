from random import choice
from string import hexdigits, punctuation
import time

base_time = str(time.time())[12:16]
print(time.time())
base_string = ''.join(choice(hexdigits) for i in range(6))
print(hexdigits)
base_punctuation = ''.join(choice(punctuation) for j in range(2))
print(punctuation)

print(base_string + base_punctuation + base_time)
