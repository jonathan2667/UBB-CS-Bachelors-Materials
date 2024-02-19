import numpy as np

#  Define the function
def f(x):
    return np.exp(-x**2)

#Define the trapezoidal rule
def trapezoidal_rule(func, a, b, n):
    h = (b - a) / n
    s = func(a) + func(b)

    for i in range(1, n):
        s += 2 * func(a + i * h)

    return (h / 2) * s

#Call the function
for a in range(0, 20):
    result = trapezoidal_rule(f, -a, a, 1000)
    print(f"For a={a}, integral value is approximately {result} and we know that sqrt(pi) is aproximately {np.sqrt(np.pi)}")