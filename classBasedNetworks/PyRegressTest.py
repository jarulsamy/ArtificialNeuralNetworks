# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import torch
import torch.nn as nn
from pyRegress import fitLine
from torch.autograd import Variable

input_dim = 1
output_dim = 1

x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]

epochs = 2000
learning_rate = 0.01

f = fitLine(input_dim, output_dim)
f.setVals(x, y)
predicted = f.regress(epochs, learning_rate)
print(predicted)
