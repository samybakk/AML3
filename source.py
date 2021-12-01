# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 16:06:31 2016

@author: Claire Vernade
"""
import numpy as np
from random import random, randint

# from random import betavariate
from math import log




def ETC(t,n_arms, m, rewards, draws):
    
    if t >= m * n_arms:
        a = np.argmax(rewards)
 
    else :
        a = t%4
    return a

def eGreedy(n_arms, epsilon, rewards, draws):
    if random() < 1-epsilon:
        a = np.argmax(rewards)
    
    else:
        a = randint(0,3)
    return a
    

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


def computeLowerBound(n_arms, true_means):
    bound =0
    
    for mean in true_means[1:] :
        dA = true_means[0] - mean
        bound += np.log(n_arms)*dA/kl(mean,true_means[0])
        
    return bound
