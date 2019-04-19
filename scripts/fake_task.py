#!/usr/bin/python3

import numpy as np

DEFAULT_ACTIVATION_WEIGHT = .5
pio_ermsg = "Input array is of length: {} | weights array is of length: {}"
def mse(v1, v2):
    return ((v1-v2)**2).mean(ax=0)

# take derivative w/respect to v1,
# where v2 is gold set

# signal receiving perceptron contains the weights

class Perceptron:

    def __init__(self,n_inputs, n_outputs, activation_weight=DEFAULT_ACTIVATION_WEIGHT):
        self.input_weights = [np.float64() for i in range(len(n_inputs))]
        self.n_outputs = n_outputs # idx corresponds to inputs in next layer
        self.threshold=activation_weight
        self.knsize = 1

    def _set_input_weights(self, arr):
        if len(arr) != len(self.input_weights):
            raise IndexError(pio_ermsg.format(len(arr), len(self.input_weights)))
        self.input_weights = arr

    def _update(self, wval, step_size):
        total = (self.ksize*self.threshold) + wval
        self.ksize += 1
        self.threshold =  total / self.ksize


        


class FFNet:

    def __init__(self, **kwargs):
        matmap = [len(kwargs['input'])] + kwargs['hidden_plan'] + [len(kwargs['output']]
        self.net = [[Perceptron(matmap[i], matmap[i+1]) for i in range(len(matmap)-1)] 
                                                         for i in range(len(matmap))]
        self.lossf = kwargs['lossf']
        self.depth = len(matmap)
        self.


    def learn(self, invec):
        pos = 0
        self._set_input_weights(invec)
        while i < len(self.net):
            i += 1



            
        






