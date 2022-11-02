import numpy as np
import random

def train_test(known_values, test_size=0.2):
    
    train_length = int(len(known_values)*(1-test_size))
    
    random.shuffle(known_values)
    training = known_values[:train_length]
    testing = known_values[train_length:]
    
    return training, testing


def RMSE(R, R_pred, values):
    error = 0

    for u,i in values:
        error += (R_pred[u, i] - R[u, i])**2
    
    return (error/len(values))**.5


def MAE(R, R_pred, values):
    error = 0

    for u,i in values:
        error += abs(R_pred[u, i] - R[u, i])
    
    return (error/len(values))

def RMSE_list(list1, list2):
    error = 0

    for ind in range(len(list1)):
        error += (list1[ind] - list2[ind])**2
    
    return (error/len(list1))**.5