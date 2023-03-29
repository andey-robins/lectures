import re
from time import time


def time_backtrack(n=1):
    start = time()
    re.match(r'(D+)+$', 'D'*n + '!')
    return time() - start


for i in range(1, 40):
    print(i, ':=', time_backtrack(i))
