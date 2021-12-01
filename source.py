# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 16:06:31 2016

@author: Claire Vernade
"""
import numpy as np
from random import random, randint

# from random import betavariate
from math import log


def eGreedy(n_arms, epsilon, rewards, draws):
    c=0
#    TODO 
    return c

def ETC(n_arms, m, rewards, draws):
    c=0
#    TODO 
    return c

def UCB(t, alpha, rewards, draws):
    if np.sum(draws == 0) > 0:
            c = np.where(draws == 0)[0][0]
    else:
        indices = rewards / draws  # TODO
        winners = np.argwhere(indices == np.max(indices))
        c = np.random.choice(winners[0])

    return c


def Thompson(n_arms, rewards, draws):
    indices = np.zeros(n_arms)
    for arm in np.arange(n_arms):
        indices[arm] = rewards / draws  # TODO
    winners = np.argwhere(indices == np.max(indices))
    c = np.random.choice(winners[0])
    return c


def kl(a, b):
    return a * log(a / b) + (1 - a) * log((1 - a) / (1 - b))


def computeLowerBound(horizon, true_means):
    bound = []
    for mean in true_means[1:] :
        bound.append(log(horizon,10)/kl(mean,true_means[0]))
        
    print(bound)
    return np.min(bound)
