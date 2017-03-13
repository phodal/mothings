from random import choice
from string import hexdigits, punctuation
import time

base_time = str(time.time())[12:16]
base_string = ''.join(choice(hexdigits) for i in range(6))
base_punctuation = ''.join(choice(punctuation) for j in range(2))

print(base_string + base_punctuation + base_time)
