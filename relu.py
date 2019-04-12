'''
relu activation function
if x>0, relu(x) = x
else relu(x)=0
x is array (batch, something)
all shape of x is ok.
'''

import numpy as np
import chainer
from chainer import cuda
import cupy as cp

class relu(object):
  def forward(self, x):
    xp = chainer.cuda.get_array_module(x)
    return xp.max(0,x)
  def backword(self.dy):
    xp = chainer.cuda.get_array_module(dy)
    return xp.max(0,dy)