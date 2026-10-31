import numpy as np
import math

def function(x):
    return math.exp(x) / (1 + x**2)

n = 10000

sum = 0

for i in range (n):
    x = np.random.uniform(0, 1)
    y = function(x)
    sum += y

mean = sum / n

print(mean)