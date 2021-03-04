import random
import string

N  = int(input())

print(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N)))
