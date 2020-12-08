import numpy as np


def sum_pair_equals(values, val_eq):
    values = np.array(values)
    return np.where(values + values[:, None] == val_eq)[0]


def sum_triad_equals(values, val_eq):
    values = np.array(values)
    sum_ = values + values[:, None] + values[:, None, None]
    return np.array(np.where(sum_ == val_eq))[:, 0]
