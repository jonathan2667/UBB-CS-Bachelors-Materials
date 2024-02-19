import numpy as np
import matplotlib.pyplot as plt
"""
As b gets smaller, the contours of f become more elongated, and the gradient descent takes more zigzagging steps and requires more iterations to converge to the minimum. 
This is because the condition number of the Hessian matrix of f (which is a measure of the elongation of the contours) increases as b decreases.
"""
def quadratic_function(x, y, b):
    return 0.5 * (x**2 + b * y**2)

def gradient_of_function(x, y, b):
    return np.array([x, b * y])

def perform_gradient_descent(initial_x, initial_y, b, learning_rate, iterations):
    current_x = initial_x
    current_y = initial_y
    history_of_points = [(current_x, current_y)]
    for _ in range(iterations):
        current_gradient = gradient_of_function(current_x, current_y, b)
        current_x -= learning_rate * current_gradient[0]
        current_y -= learning_rate * current_gradient[1]
        history_of_points.append((current_x, current_y))
    return history_of_points

figure, axes = plt.subplots(2, 2, figsize=(10, 10))  # Create a 2x2 grid of subplots
axes = axes.ravel()  # Flatten the array of axes for easy iteration

for index, b_value in enumerate([1, 1/2, 1/5, 1/10]):
    points_history = perform_gradient_descent(1.0, 1.0, b_value, 0.1, 100)
    points_history = np.array(points_history)
    x_values = np.linspace(-1.5, 1.5, 400)
    y_values = np.linspace(-1.5, 1.5, 400)
    X, Y = np.meshgrid(x_values, y_values)
    Z = quadratic_function(X, Y, b_value)
    axes[index].contour(X, Y, Z, 50)
    axes[index].plot(points_history[:, 0], points_history[:, 1], 'o-')
    axes[index].set_title(f'b = {b_value}')

plt.tight_layout()  # Adjust the layout to minimize overlap
plt.show()


