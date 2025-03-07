import numpy as np
from scipy import stats

def get_random_number(mean, std):
    return round(np.random.normal(mean, std), 2)

get_random_number(10, 3)