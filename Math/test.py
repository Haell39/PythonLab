import matplotlib.pyplot as plt
import numpy as np
import sympy as sy
import math

def f(x):
    return x ** 2
    x = sy.symbols('x')

print(sy.integrate(f(x), (x, 0, 2)))
