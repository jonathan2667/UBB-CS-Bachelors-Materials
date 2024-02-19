import numpy as np
from typing import Callable, Tuple, List

# Define the function and its gradient
def f(x: np.ndarray) -> float:
    return x[0]**2 + 3*x[1]**2

def grad_f(x: np.ndarray) -> np.ndarray:
    df_dx = 2*x[0]
    df_dy = 6*x[1]
    return np.array([df_dx, df_dy])

def hessian_f(x: np.ndarray) -> np.ndarray:
    return np.array([[2, 0], [0, 6]])

def newton(x: np.ndarray, f: Callable, gf: Callable, hf: Callable, lr=0.01, lr_decr=0.999, maxiter=100, tol=0.001) -> Tuple[np.ndarray, List[np.ndarray], int]:
    points = [x]
    nit = 0
    for _ in range(maxiter):
        gradient = gf(x)
        hessian = hf(x)
        x_new = x - np.linalg.inv(hessian).dot(gradient)

        if np.linalg.norm(x_new - x) < tol:
            break

        x = x_new
        nit += 1
        points.append(x)

    return x, points, nit

# Initialize x
x = np.array([2, 2])

# Apply Newton's method
x_min, points, nit = newton(x, f, grad_f, hessian_f)

print(f"Newton's method converged to the minimum at {x_min} in {nit} iterations.")