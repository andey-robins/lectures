import re
from time import time
from tqdm import tqdm
import math
import numpy as np
from sklearn.linear_model import LogisticRegression


def backtrack_match(s):
    re.match(r'((D+)+)$', s)


def time_backtrack(n=1):
    start = time()
    backtrack_match('D'*n + '!')
    return time() - start


def unit_test():
    MIN_SUPPORTED_SIZE = 50
    MAX_SUPPORTED_TIME = 600

    X, y = [], []
    for i in tqdm(range(22, 27)):
        X.append(time_backtrack(i))
        y.append(i)

    X, y = np.array(X), np.array(y)
    model = np.polyfit(X, np.log(y), 1)
    prediction = np.exp(model[1]) * np.exp(model[0] * MIN_SUPPORTED_SIZE)

    if prediction > MAX_SUPPORTED_TIME:
        print(
            f'Estimated time of {prediction} was greater than limit {MAX_SUPPORTED_TIME}')


unit_test()
